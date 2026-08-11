from fastapi import APIRouter,UploadFile,File,HTTPException,status,Depends
from app.services.ingestion import ingest_document
from app.services.vector_store import VectorStore
from app.services.chunking import chunk_text
from app.services.embeddding import get_embedding
import tempfile
import os

router = APIRouter(prefix="/documents",tags=["Documents"])
vector_store = VectorStore()

#upload Endpoint
@router.post("/upload")
def post_upload(file:UploadFile= File(...)):

    content = file.filename
    with tempfile.NamedTemporaryFile(delete=False,suffix ="") as tmp:
        tmp.write(file.file.read())
        tmp.path = tmp.name

        doc=ingest_document(tmp.path)
        chunks =chunk_text(doc.content,500,50)

        embeddings = [get_embedding(chunk) for chunk in chunks]

        ids= [f"{doc.id}_{i}"for i in range(len(chunks))]
        metadatas = [{"doc_id":doc.id} for i in chunks]
    
        vector_store.add_documents(chunks,ids,metadatas,embeddings)
        os.unlink(tmp.path)

    return {"message":"uploadFile sucessfully","filename":file.filename,"chunks":len(chunks)}


#list Endpoint
@router.get("/")
def get_list():
    return{"documents":[]}

#delete Endpoint
@router.delete("/{doc_id}")
def delete_document(doc_id:str):
    return {"message":f"delete:{doc_id}deleted"}


if "__name__"=="__main__":

    print("documents installed successfully")