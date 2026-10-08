from pytest import raises
from pathlib import Path
from rag.document.loaders.text_loader import TextLoader
from rag.document.document_structs import Document

def test_load_text_file_exists():
    loader = TextLoader()
    sample_path = Path(__file__).parent / "sample.txt"
    document = loader.load(str(sample_path))

    assert isinstance(document, Document)
    assert isinstance(document.text, str)
    assert isinstance(document.metadata, dict)

    sample_text = """hi, this is a sample test document


end of file"""

    assert document.text == sample_text
    assert document.metadata == {"source": "sample.txt"}

def test_load_text_file_not_exists():
    loader = TextLoader()
    with raises(FileNotFoundError, match="File not found: non_existent_file.txt"):
        loader.load("non_existent_file.txt")