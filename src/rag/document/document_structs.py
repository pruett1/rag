from dataclasses import dataclass
from typing import Any

@dataclass
class Document:
    text: str
    metadata: dict[str, Any]

@dataclass
class DocumentChunk:
    text: str
    metadata: dict[str, Any]
    chunk_index: int