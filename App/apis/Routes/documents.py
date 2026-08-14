from fastapi import APIRouter,UploadFile,File,HTTPException,status,Depends
from app.services.ingestion import ingest_document
from app.services.vector_store import VectorStore
from app.services.chunking import chunk_text
from app.services.embeddding import get_embedding
from app.core.auth import get_current_user
import tempfile
import os

router = APIRouter(prefix="/documents",tags=["Documents"])
vector_store = VectorStore()

#upload Endpoint
@router.post("/upload")
def post_upload(file:UploadFile= File(...),Current_user:dict = Depends(get_current_user)):

    file_ext = os.path.splitext(file.filename)[1]
    
    with tempfile.NamedTemporaryFile(delete=False,suffix =file_ext) as tmp:
        content = file.file.read()
        tmp.write(content)
        tmp_path = tmp.name

    try:
        doc=ingest_document(tmp.name)
        chunks = chunk_text(doc.content, 500, 50)
        if not chunks:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=("File contains no readable text or is empty")
        )

        embeddings = [get_embedding(chunk) for chunk in chunks]

        ids= [f"{doc.id}_{i}"for i in range(len(chunks))]
        metadatas = [{"doc_id":doc.id} for i in chunks]
    
        vector_store.add_documents(chunks,ids,embeddings,metadatas)
        os.unlink(tmp_path)

        return {"message":"uploadFile sucessfully","uploaded_by" : Current_user.get("sub") ,"filename":file.filename,"chunks":len(chunks)}

    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            details =f"Error processing file :{str(e)}"
        )



    finally:
        if os.path.exists(tmp_path):
            try:
                os.unlink(tmp_path)
            except PermissionError:
                # File is locked, try again after short delay
                import time
                time.sleep(0.1)
                try:
                    os.unlink(tmp_path)
                except:
                    pass
#list Endpoint
@router.get("/")
def get_list():
    return{"documents":[]}

#delete Endpoint
@router.delete("/{doc_id}")
def delete_document(doc_id:str):
    return {"message":f"delete:{doc_id}deleted"}


if __name__=="__main__":

    print("documents installed successfully")