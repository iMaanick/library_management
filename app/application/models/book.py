import enum
from dataclasses import dataclass


class BookStatus(str, enum.Enum):
    AVAILABLE = "в наличии"
    ISSUED = "выдана"


@dataclass
class Book:
    id: int
    title: str
    author: str
    year: int
    status: BookStatus = BookStatus.AVAILABLE
