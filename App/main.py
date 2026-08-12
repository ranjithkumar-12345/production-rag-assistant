from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.apis.Routes import query,documents
from app.apis.denpendencies import RAGPipeline,Retriever,llm,VectorStore

app = FastAPI(
    TITLE= "PRODUCTION RAG ASSISTANT",
    DESCRIPTION= "AI POWERED RAG ASSISTANT WITH THE documents",
    VERSION = "0.1"
)

app.add_middleware(
    CORSMiddleware,
    allow_methods = ["*"],
    allow_credentials = True,
    allow_origins = ["*"],
    allow_headers =["*"]
)

app.include_router(query.router)
app.include_router(documents.router)

@app.get("/")
def root():
    return {"message":"rag assistant is working successfully"}

@app.get("/health")
def root():
    return {"status:ok"}