from app.services.embeddding import get_embedding
from app.services.vector_store import VectorStore
from app.config import settings

class Retriever():
    def __init__(self):
        self.vector_store = VectorStore

    def retrive(self,query:str,top_k :int = settings.TOP_K):
        query_embeddings = get_embedding(query)

        results = self.vector_store.search(query_embeddings,top_k)

        return results


if __name__ =="__main__":
    retrive =Retriever()

    print("retrive intialize sucessfully")