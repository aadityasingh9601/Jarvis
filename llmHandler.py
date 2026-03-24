from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key=api_key)

def callLLM(command):
    response = client.models.generate_content(
    model="gemini-3-flash-preview",
    config=types.GenerateContentConfig(
        system_instruction="You are a personal voice assistant. Your name is Jarvis. Reply to everything in short."),
    contents=command,
    )
    
    print(response.text)
    return response.text