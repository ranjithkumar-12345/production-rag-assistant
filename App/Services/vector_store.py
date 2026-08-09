import chromadb
from chromadb.config import Settings
from app.config import settings


class VectorStore:
    VECTOR_DB_PATH = "./data/raw data"
    def __init__(self):
        self.client = chromadb.PersistentClient(
            path=settings.VECTOR_DB_PATH
        )
        self.collection = self.client.get_or_create_collection(
            name="documents"
        )

    def add_documents(self, ids, documents, embeddings, metadatas):
        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )

    def search(self, query_embedding, top_k=5):
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        return results


if __name__ == "__main__":
    store = VectorStore()
    print("✅ VectorStore initialized successfully!")