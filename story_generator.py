import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

def generate_story(genre, character, setting, tone, length):
    prompt = (
        f"Write a {length.lower()} {tone.lower()} {genre.lower()} story "
        f"about a character named {character} in a {setting}."
    )

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "DeepSeek-R1-Distill-Llama-70B",  # Groq’s default for fast, creative tasks
        "messages": [
            {"role": "system", "content": "You are a creative storyteller AI."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions", json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f" Error: {response.status_code} - {response.text}"
