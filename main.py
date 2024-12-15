from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from bs4 import BeautifulSoup
import openai
import requests

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

openai.api_key = "YOUR_OPENAI_API_KEY"

def identify_intent(message, pages_visited):
    prompt = f"""
    Identify the intent of the user based on the following:
    - Message: {message}
    - Pages Visited: {pages_visited}
    Provide a concise summary of the user's intent.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant that identifies user intent."},
            {"role": "user", "content": prompt}
        ],
        temperature=0,
        top_p=1
    )
    return response['choices'][0]['message']['content'].strip()

def scrape_page_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.title.string if soup.title else "No title available"
    description = soup.find("meta", attrs={"name": "description"})
    description = description["content"] if description else "No description available"

    return {"url": url, "title": title, "description": description}

def process_pages(pages_visited):
    combined_content = []
    for url in pages_visited:
        page_content = scrape_page_data(url)
        combined_content.append(page_content)
    return combined_content

def combine_context(message, scraped_content):
    combined = f"User Message: {message}\n\nScraped Content:\n"
    for content in scraped_content:
        combined += f"URL: {content['url']}\nTitle: {content['title']}\nDescription: {content['description']}\n\n"
    return combined

def generate_email(intent, scraped_data):
    prompt = f"""
    Generate a professional email based on the following:
    - User Intent: {intent}
    - Scraped Data: {scraped_data}
    Use the following structure:
    - Greeting
    - Address the user's intent
    - Highlight relevant case studies
    - Include company introduction and portfolio links
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant that creates professional emails."},
            {"role": "user", "content": prompt}
        ],
        temperature=0,
        top_p=1
    )
    return response['choices'][0]['message']['content'].strip()

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("email_template.html", {"request": request})

@app.post("/analyze-urls/")
async def generate_email_page(request: Request, message: str = Form(...), pages_visited: str = Form(...)):
    pages_list = pages_visited.split(",")
    intent = identify_intent(message, pages_list)
    scraped_data = process_pages(pages_list)
    email_content = generate_email(intent, scraped_data)

    return templates.TemplateResponse("email_template.html", {
        "request": request,
        "email_content": email_content,
        "message": message,
        "pages_visited": pages_visited
    })
