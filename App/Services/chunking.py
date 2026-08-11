from pathlib import Path
from typing import Dict, List, Any

def chunk_text(text:str,chunk_size:int,overlap:int):
    text : str
    chunk_size : int
    overlap : int
    chunks = []
    start = 0
    while  start < len(text):
        end = start+chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end -overlap
    return chunks


if __name__ == "__main__":

    chunk_size = 50
    over_lap = 5
    sample_text = "This is a sample text for testing chunking functionality."
    chunk = chunk_text(sample_text, 500, 50)
    print(f"Total chunks: {len(chunk)}")
    for i, chunk in enumerate(chunk):
        print(f"Chunk {i+1}: {chunk[:100]}...")
