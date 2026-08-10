import os
import google.genai as genai
from app.services.retrieval import Retriever
from app.services.llm import LLM
from dotenv import load_dotenv

load_dotenv()

class RAGPipeline():
    def __init__(self):
        self.Retriver = Retriever()

        self.client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))
        self.model = "gemini-1.5-flash"


    def query(self,question:str,context:str):

        prompt = f"context:{context}\n\nQuestion:{question}\n\nAnswer"
        response = self.client.models.generate.content(
            models=self.model,
            context = prompt
        )

        return response.text


if __name__=="__main__":

    rag = RAGPipeline()
    print("rag_pipeline successfully initialized")
