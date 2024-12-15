# API Development and Business Proposal - OpenAI

This project identifies the user's intent by analyzing the "message section" and "pages visited." It generates a customized email template based on the extracted intent.

The project uses OpenAI model API implemented.

### Features :

Accepts user input (name, email, message, and pages visited),
<br/>Scrapes relevant data from the provided URLs,
<br/>Uses an LLM to generate a customized email,
<br/>Returns the generated email response.

### Prerequisites :

Python 3.9 or later

### Running Locally :

git clone https://github.com/Dilip-code/email_generate_openai.git

cd email_generate_openai

pip install -r requirements.txt

uvicorn main:app --reload

The API will be running at: http://127.0.0.1:8000

### Running with Docker :

docker build -t email_generate_openai_3.9 .

docker run -p 8000:8000 email_generate_openai_3.9

The API will be accessible at: http://127.0.0.1:8000




### Input :

Message : Need Go and Web developers

Pages Visited : 

https://www.mindinventory.com/golang-development.php,
https://www.mindinventory.com/hire-ai-developers.php,
https://www.mindinventory.com/healthcare-solutions.php


### Output 

Generated Email:

Subject: Re: Inquiry for Hiring Go and Web Developers

Dear [User],

I hope this email finds you well. I understand that you are in need of Go and Web developers for your upcoming projects. Based on your interest in Go development and AI developers, I have identified some relevant resources that align with your requirements.

I came across your visit to the following pages related to Go development and AI engineers:

1. Golang Development Company | Golang Web Development Services
   - URL: [https://www.mindinventory.com/golang-development.php]
   - Description: MindInventory is a top-notch Golang development company, offering highly skilled Golang developers for custom web applications.

2. Hire AI Developers | AI Engineers for Hire
   - URL: [https://www.mindinventory.com/hire-ai-developers.php]
   - Description: Looking to hire AI developers to build AI-powered solutions? Our team of AI engineers can help shape your business ideas into reliable software solutions.

I would like to introduce our company, [Your Company Name], a leading software development firm specializing in Go and Web development. We have a proven track record of delivering high-quality solutions to our clients. You can explore our portfolio and case studies on our website [Your Company Portfolio Link].

If you are interested in discussing your project requirements further or would like to explore how we can assist you in hiring Go and Web developers, please feel free to reach out to us.

Thank you for considering [Your Company Name]. We look forward to the opportunity to collaborate with you on your upcoming projects.

Best regards,

[Your Name]
[Your Position]
[Your Company Name]
[Contact Information]
