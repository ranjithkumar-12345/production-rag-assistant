import os
from dotenv import load_dotenv
from pydantic_settings  import BaseSettings

load_dotenv()

class Settings(BaseSettings):

    GEMINI_API_KEY : str
    GEMINI_MODEL : str 
    GEMINI_EMBEDDING_MODEL : str

#chuncking
    CHUNK_SIZE: int= 500
    CHUNK_OVERLAP:int =50
    
#retrival
    TOP_K:int =5
    
#llm
    Max_Tokens: int = 2000
    Temperature:float = 0.7

#vector DB_path

    VECTOR_DB_PATH: str 
    LOG_FILE: str 

    Debug:bool=True

class Config:
    env_file = ".env"
    env_file_encoding = "utf-8"


def get_settings():
    return Settings

settings = Settings()

if __name__ == "__main__":
    settings = Settings()
    print(f"API Key: {settings.GEMINI_API_KEY[:10]}...")
    print(f"Model: {settings.GEMINI_MODEL}")
    print(f"Chunk Size: {settings.CHUNK_SIZE}")

