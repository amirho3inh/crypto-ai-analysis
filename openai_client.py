from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

class OpenAIClient:
    def __init__(self):
        # api_key =
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY is not set in environment variables.")
        self.client = OpenAI(api_key=api_key,)

    def get_response(self, prompt, model="chatgpt-4o-latest", stream=False):

        try:
            response = self.client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model=model,
                stream=stream,
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {e}"
