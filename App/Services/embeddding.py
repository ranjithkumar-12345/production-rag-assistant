import os
from dotenv import load_dotenv
import google.genai as genai

load_dotenv()

client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))
def get_embedding(text:str):

    result = client.models.embed_content(
        model = "gemini-embedding-001",
        contents = text 
    )
    return result.embeddings[0].values


if __name__ =="__main__":

    embedding = get_embedding("My name is ranjith")
    print(len(embedding))
    print(embedding[:6])
