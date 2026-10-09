from pytest import raises

from rag.document.document_structs import Document, DocumentChunk
from rag.document.chunk import fixed_size_chunks

def test_fixed_size_chunks():
    document = Document(text="This is a test docoument for chunking.", metadata={"source": "test input"})
    chunk_size = 10
    overlap = 2

    chunks = fixed_size_chunks(document, chunk_size, overlap)
    expected_chunk_texts = ["This is a ", "a test doc", "ocoument f", " for chunk", "nking."]

    assert len(chunks) == len(expected_chunk_texts)
    for i, chunk in enumerate(chunks):
        assert isinstance(chunk, DocumentChunk)
        assert chunk.text == expected_chunk_texts[i]
        assert chunk.metadata == document.metadata
        assert chunk.chunk_index == i

def test_fixed_size_chunks_invalid_parameters():
    document = Document(text="This is a test docoument for chunking.", metadata={"source": "test input"})

    with raises(ValueError, match="chunk_size must be greater than 0"):
        fixed_size_chunks(document, chunk_size=0)

    with raises(ValueError, match="overlap must be non-negative"):
        fixed_size_chunks(document, chunk_size=10, overlap=-1)

    with raises(ValueError, match="overlap must be less than chunk_size"):
        fixed_size_chunks(document, chunk_size=10, overlap=10)