import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
chave = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=chave)

for modelo in client.models.list():
    print(modelo.name)
