from fastapi import APIRouter,UploadFile,File
from app.services.ingestion import ingest_document

router = APIRouter(prefix="/documents",tags=["Documents"])


#upload Endpoint
@router.post("/upload")
def post_upload(file:UploadFile= File(...)):

    content = file.filename

    return {"message":"uploadFile sucessfully","filename":file.filename}

#list Endpoint
@router.get("/")
def get_list():
    return{"documents":[]}

#delete Endpoint
@router.delete("/{doc_id}")
def delete_document(doc_id:str):
    return {"message":f"delete:{doc_id}deleted"}


if "__name__"=="__main__":

    post_upload()
    get_list()
    delete_document()