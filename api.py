from openai import OpenAI
import os
from dotenv import load_dotenv


def get_response(split_list) -> str:
    load_dotenv()
    client = OpenAI(
        api_key=os.getenv("API_KEY")
    )
    
    
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
        {"role": "assistant", "content": "Provide some questions and answers regarding the text"},
        {"role": "user", "content": split_list[0]}
    ]
    )
    
    return response.choices[0].message.content