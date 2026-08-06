from datetime import datetime
import os
import uuid
from pydantic import BaseModel,Field,field_validator
from typing import Optional,List,Dict,Any

class ChunkCreateModel(BaseModel):
    "creating the chunks "
    document_id:str
    content:Optional[str]
    metadata:Dict[str,Any]=Field(default_factory =dict)
    index:int

class ChunkCreate(ChunkCreateModel):
    "full chunk model with embedding"
    id:str =Field(default_factory=lambda: str(uuid.uuid4()))
    embedding:Optional[List[float]]=None
    embedding_length:Optional[int] =None

class ChunkResponse(BaseModel):
    "Response the chunks from metadata after cleaning the pdf"
    id:str
    document_id:str
    content:Optional[str]
    metadata:Dict[str,Any]=Field(default_factory =dict)
    index:int
    similarity_score:Optional[float]=None

if __name__ =="__main__":

    chunk = ChunkCreateModel(
            document_id ="001",
            content = "ranjith is working on a top tech multinational company with ctc 32 lpa",
            index = 1
)
    print("chunkcreatemodel wors sucessfully")

    chunk_embedding = ChunkCreate(
        document_id = "001",
        content = "test content",
        index = 2,
        embedding = [0.1,0.3,0.4],
        embedding_length =10
    )

    print(f"ChunkCreate:{chunk_embedding.id}")

    chunk_response = ChunkResponse(
        id ="010",
        document_id ="001",
        content = "ranjith is working on a top tech multinational company with ctc 32 lpa",
        similarity_score=0.95,
        index = 1
    )
    print(f"response:{chunk_response.similarity_score}")