from fastapi import FastAPI,APIRouter
from app.models.response import QueryRequest,QueryResponse
from app.services.rag_pipeline import RAGPipeline
from app.services.vector_store import VectorStore
from app.services.embeddding import get_embedding


app = FastAPI()

router = APIRouter(prefix="/query", tags=["Query"])

vector_store = VectorStore()
rag = RAGPipeline()

@router.post("/")
def get_query(request:QueryRequest):
    query_vector = get_embedding(request.query)
    search_results = vector_store.search(query_vector, top_k=request.top_k)
    if search_results and search_results.get("documents"):
        context = "\n\n".join(search_results["documents"][0])
    else:
        context = "No relevant context found."
    answer=rag.query(question=request.query,context = context)
    response = QueryResponse(
        query = request.query,
        answer=answer,
        model ="gemini-flash-latest" 
        )
    return response


if __name__=="__main__":
    print("query router installed")
