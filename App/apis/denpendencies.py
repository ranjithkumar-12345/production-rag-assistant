from app.services.vector_store import VectorStore
from app.services.rag_pipeline import RAGPipeline
from app.services.retrieval import Retriever
from app.services.llm import LLM

vector_store = VectorStore()
rag_pipeline = RAGPipeline()
retrieval =Retriever()
llm = LLM()

def get_vector_store():
    return vector_store

def get_rag_pipeline():
    return rag_pipeline

def get_retrieval():
    return retrieval

def get_llm():
    return llm


if __name__=="__main__":

    print("Dependencies initialized successfully!")
    print(f"VectorStore: {vector_store}")
    print(f"RAGPipeline: {rag_pipeline}")
    print(f"Retriever: {retrieval}")
    print(f"LLM: {llm}")