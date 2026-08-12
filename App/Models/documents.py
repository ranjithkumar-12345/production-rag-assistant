"""
Document data models for RAG System
"""
from datetime import datetime, timezone
from typing import Optional, List, Dict, Any
from enum import Enum
from pydantic import BaseModel, Field, field_validator
import uuid


class DocumentStatus(str, Enum):
    """Document processing status"""
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class DocumentCreate(BaseModel):
    """Model for creating a new document"""
    filename: str
    content: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)
    
    @field_validator('filename')
    @classmethod
    def validate_filename(cls, v: str) -> str:
        """Validate file extension is allowed"""
        allowed = ['.pdf', '.docx', '.txt', '.md', '.html']
        ext = v.lower()
        # Check if any allowed extension matches
        if not any(v.lower().endswith(ext) for ext in allowed):
            raise ValueError(f"File type not allowed. Allowed: {allowed}")
        return v


class Document(BaseModel):
    """Full document model with database fields"""
    filename: str
    content: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    filename: str
    status: DocumentStatus = DocumentStatus.PENDING
    chunks: int = 0
    chunk_ids: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    error_message: Optional[str] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class DocumentResponse(BaseModel):
    """Response model for document operations"""
    id: str
    filename: str
    status: DocumentStatus
    total_chunks: int = 0
    created_at: datetime
    error_message: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)


# Test code (optional)
if __name__ == "__main__":
    # Test DocumentCreate
    doc = DocumentCreate(filename="test.pdf")
    print(f"Document created: {doc.filename}")
    
    # Test Document
    full_doc = Document(filename="test.pdf")
    print(f"Document ID: {full_doc.id}")
    print(f"Status: {full_doc.status}")