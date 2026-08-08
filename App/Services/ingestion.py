from pathlib import Path
from app.models.documents import DocumentCreate
from app.utils.file_handlers import read_pdf, read_docx, read_html, read_txt


def get_extension(file_path: str):
    return Path(file_path).suffix.lower()


def ingest_document(file_path: str):
    extension = get_extension(file_path)
    
    # 1. Content Extract
    if extension == ".pdf":
        content = read_pdf(file_path)
    elif extension == ".docx":
        content = read_docx(file_path)
    elif extension == ".txt":
        content = read_txt(file_path)
    elif extension == ".html":
        content = read_html(file_path)
    else:
        raise ValueError(f"Unsupported file type: {extension}")
    
    # 2. Document Create (అన్ని cases కి common)
    doc = DocumentCreate(
        filename=Path(file_path).name,
        content=content
    )
    
    print(f"✅ Document ingested: {doc.filename}")
    print(f"📄 Content length: {len(content)} characters")
    return doc


if __name__ == "__main__":
    # Test
    doc = ingest_document(r"C:\Users\hp\Downloads\Document.txt")
    
    # Document object నుండి content తీయడం
    print("\n" + "=" * 50)
    print("📄 FIRST 500 CHARACTERS:")
    print("=" * 50)
    print(doc.content[:500])  # ← .content use చేయాలి
    print("=" * 50)
    print(f"📊 Total characters: {len(doc.content)}")
    print(f"📁 Filename: {doc.filename}")