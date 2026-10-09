from rag.document.loaders.text_loader import TextLoader
from rag.document.document_structs import Document

class Loader:
    def __init__(self):
        self.text_loader = TextLoader()

    def load(self, file_path: str) -> Document:
        if file_path.endswith('.txt'):
            return self.text_loader.load(file_path)
        else:
            raise ValueError(f"Unsupported file type: {file_path}")
