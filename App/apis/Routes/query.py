from fastapi import FastAPI,APIRouter
from app.models.response import QueryRequest,QueryResponse
from app.services.rag_pipeline import RAGPipeline as rag


app = FastAPI()

router = APIRouter(prefix="/query", tags=["Query"])

@router.post("/")
def get_query(request:QueryResponse):
    answer=rag.query(request.query)
    response = QueryResponse(
        query = request.query,
        answer=answer,
        model = "gemini-1.5-flash"
        )
    return response


if __name__=="__main__":
    print("query router installed")
