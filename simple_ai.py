import os
from langchain.chat_models import init_chat_model

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

model = init_chat_model(
    model="gemini-3-flash-preview",
    model_provider="google-genai",
    api_key=GOOGLE_API_KEY
)

response = model.invoke("Hey, how're you today?")
response_str = response.content
print(response_str)

