from rag.document.document_structs import Document
from pathlib import Path

class TextLoader:
    def __init__(self):
        pass

    def load(self, file_path: str) -> Document:
        if not Path(file_path).exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        text = Path(file_path).read_text(encoding='utf-8')
        metadata = {"source": Path(file_path).name}
        return Document(text=text, metadata=metadata)