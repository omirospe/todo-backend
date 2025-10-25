from datetime import datetime
from ..base_entity import BaseEntity
from typing import Any


class TodoEntity(BaseEntity):
    def __init__(
            self,
            id: str | None = None,
            title: str = None,
            description: str = None,
            created_at: datetime | None = None,
            updated_at: datetime | None = None,
            deleted_at: datetime | None = None
    ):
        self.id = id
        self.title = title
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at

        self._validate()

    def _validate(self):
        if len(self.title.replace(" ", "")) < 5:
            raise ValueError('Title should be more than 5 characters long')

    def update_description(self, description: str):
        self.description = description

        self._validate()
