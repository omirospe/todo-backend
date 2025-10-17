from dataclasses import dataclass
from datetime import datetime


@dataclass
class TodoDTO:
    title: str
    description: str
    id: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    deleted_at: datetime | None = None
    