import os
import google.genai as genai
from app.services.retrieval import Retriever
from app.services.llm import LLM
from dotenv import load_dotenv

load_dotenv()

class RAGPipeline():
    def __init__(self):
        self.retriever = Retriever()
        api_key = os.getenv("GEMINI_API_KEY")

        self.client = genai.Client(api_key = api_key)
        if not api_key:
                    raise ValueError("GEMINI_API_KEY environment variable is missing! Check your .env file.")

        self.model = "gemini-flash-latest"


    def query(self,question:str,context:str):

        prompt = f"context:{context}\n\nQuestion:{question}\n\nAnswer"
        response = self.client.models.generate_content(
            model=self.model,
            contents = prompt
        )

        return response.text


if __name__=="__main__":

    rag = RAGPipeline()
    print("rag_pipeline successfully initialized")
