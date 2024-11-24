from dataclasses import dataclass
from enum import Enum


class BookStatus(str, Enum):
    AVAILABLE = "в наличии"
    ISSUED = "выдана"


@dataclass
class Book:
    id: int
    title: str
    author: str
    year: int
    status: BookStatus = BookStatus.AVAILABLE
