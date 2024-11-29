from dotenv import load_dotenv
import os
from huggingface_hub import InferenceClient

load_dotenv()

class HuggingfaceAIClient:
    def __init__(self):
        api_key = os.getenv("HUGGINGFACE_API_KEY")
        if not api_key:
            raise ValueError("Huggingface API_KEY is not set in environment variables.")
        self.client = InferenceClient(api_key=api_key,)

    def get_response(self, prompt, model=os.getenv("HUGGINGFACE_MODEL"), stream=False):

        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.5,
                max_tokens=2048,
                top_p=0.7,
	            stream=stream,
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {e}"
