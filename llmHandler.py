from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("OPEN_API_KEY")

client = OpenAI(api_key=api_key)

def callLLM(command):
    response = client.responses.create(
        model="gpt-5-nano",
        # max_output_tokens=500,
        input = [
            {
                "role":"system",
                "content":"You're a voice personal assistant named Jarvis. Give short replies only please!"
            },
            {
                "role":"user",
                "content":f"{command}"
            }
        ]
        
    )

    print(response.output_text)
    return response.output_text
    
