import os
from dotenv import load_dotenv
import google.genai as genai

load_dotenv()

class LLM():
    def __init__(self):

        self.client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

        self.model = "gemini-flash-latest"

    def generate(self,context:str,questio:str,)->str:
        prompt = f"context =context\n\nQuestion=question\n\nAnswer:"
        response = self.client.models.generate_content(
            models=self.model,
            content =prompt
        )

        return response.text

if __name__ =="__main__":

    LLm = LLM()
    print("LLm intialized successfully")