import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

ENV_FILE = Path(__file__).resolve().parent.parent / "LLM Parameters" / ".env"
load_dotenv(ENV_FILE)


class TextGenerationAPIError(Exception):
    """Raised when the text generation API returns an error response."""


class TextGenerationClient:
    def __init__(self, api_url, api_key):
        self.api_url = api_url
        self.api_key = api_key

    def generate_text(self, payload):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }

        response = requests.post(self.api_url, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        raise TextGenerationAPIError(f"Error: {response.status_code} - {response.text}")


def main():
    api_url = os.getenv("API_URL")
    api_key = os.getenv("API_KEY")

    if not api_url or not api_key:
        raise ValueError(
            "Please set API_URL and API_KEY environment variables before running this script. "
            "The project already contains a .env file under 'LLM Parameters', and it will be loaded automatically."
        )

    client = TextGenerationClient(api_url, api_key)
    payload = {
        "model": "deepseek-v4-flash",
        "messages": [
            {"role": "system", "content": "你是一个短片小说创作者，写一篇短篇小说，500字以内"},
            {"role": "user", "content": "3个人物，2个情节"},
        ],
        "max_tokens": 800,
        "top_p": 1,
        "temperature": 1,
    }

    generated_text = client.generate_text(payload)
    print(generated_text)
    return generated_text


if __name__ == "__main__":
    content = main()