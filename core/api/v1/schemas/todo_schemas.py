from pydantic import BaseModel, Field
from datetime import datetime


class TodoBaseChema(BaseModel):
    title: str = Field(..., min_length=5, max_length=50)
    description: str = Field(..., min_length=10, max_length=255)


class CreateTodoSchema(TodoBaseChema):
    pass


class UpdatedTodoSchema(BaseModel):
    description: str = Field(..., min_length=10, max_length=255)


class TodoResponseSchema(TodoBaseChema):
    id: str
    created_at: datetime | None = None
    updated_at: datetime | None = None


class TodoListItemResponseSchema(BaseModel):
    id: str
    title: str
