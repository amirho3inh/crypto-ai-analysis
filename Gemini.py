from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

class GeminiAIClient:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("Gemini API_KEY is not set in environment variables.")
        genai.configure(api_key=api_key)

    def get_response(self, prompt, model=os.getenv("GEMINI_MODEL", "gemini-1.5-flash")):
        try:
            generative_model = genai.GenerativeModel(model)
            response = generative_model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error: {e}"
