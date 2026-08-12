from datetime import datetime
from pydantic import BaseModel,Field,field_validator
from typing import Optional,Any,List,Dict


class Source(BaseModel):
    document_id:str
    document_name:str
    content:str 
    chunk_id:str
    metadata:Dict[str,Any]=Field(default_factory=dict)
    score:Optional[float] = None

class QueryRequest(BaseModel):
    query:str
    top_k:int = 5
    include_sources:bool = True
    conversation_id:Optional[str]=None
    stream:bool = False

class QueryResponse(BaseModel):
    query:str
    answer:str
    conversation_id:Optional[str] = None
    processing_time:Optional[float] = 0.0
    model:str ="gemini-flash-latest"
    tokens_used:Optional[int] =0
    sources:List[Source]=Field(default_factory=list)
    created_at:datetime = Field(default_factory =datetime.now)


if __name__=="__main__":

    "Testing is underprocess"

    Model = Source(
        document_id="001",
        document_name="test.pdf",
        content="ranjith",
        chunk_id="002",
        score=0.95
    )

    print("sources are given successfully")


    Query = QueryRequest(
        query="what is my name",
        top_k=5,
        conversation_id="1",
        stream=False,
    )

    print(f"Query_request:{Query.query}")

    response = QueryResponse(
        query="what is my name ",
        model = "gemini-1.5-flash",
        answer= "ranjith",
        sources  =[Model]
    )

    print(f"response:{response.answer}")

    print(f"Sources:{len(response.sources)}")