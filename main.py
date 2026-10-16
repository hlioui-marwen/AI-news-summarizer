import requests
from send_email import send_email
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv()


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
print(NEWS_API_KEY)



url = (
    "https://newsapi.org/v2//top-headlines?"
    "category=business&"
    "language=en&"
    "pageSize=8&"
    "sortBy=publishedAt&apiKey=" + NEWS_API_KEY
)

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
articles = content["articles"]
print(articles)

# AI summarizing the news
model = init_chat_model(
    model="gemini-3-flash-preview",
    model_provider="google-genai",
    api_key=GOOGLE_API_KEY
)

prompt = f"""
You're a news summarizer.
Write a short paragraph analyzing those news.
Add another second paragraph to tell me
how they affect the stock market.
Here are the news articles:
{articles}
"""
response = model.invoke(prompt)
response_str = response.content[0]['text']

body = "Subject: News Summary\n\n" + response_str + "\n\n"

body = body.encode("utf-8")
send_email(message=body)