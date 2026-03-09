from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("OPEN_API_KEY")

client = OpenAI(api_key=api_key)

def callLLM(command):
    response = client.responses.create(
        model="gpt-5-nano",
        input=command
    )
    print(response.output_text)
    return response.output_text
    
