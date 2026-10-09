from rag.document.document_structs import Document, DocumentChunk

# TODO: make this based on tokens as opposed to characters
def fixed_size_chunks(document: Document, chunk_size: int, overlap: int = 50) -> list[Document]:
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")
    if overlap < 0:
        raise ValueError("overlap must be non-negative")
    if overlap >= chunk_size:
        raise ValueError("overlap must be less than chunk_size")

    chunks = []
    current = 0

    while current < len(document.text):
        end = min(current + chunk_size, len(document.text))
        chunk_text = document.text[current:end]
        chunks.append(DocumentChunk(text=chunk_text, metadata=document.metadata.copy(), chunk_index=len(chunks)))
        current += chunk_size - overlap

    return chunks

# TODO: add better chunking strategies (based on sentences -> based on semantic similarity)