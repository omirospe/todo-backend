from core.infra.db.todo import TodoRepository
from core.infra.db import get_db
from fastapi import Depends
from core.application.services import TodoService


def get_todo_repository(db=Depends(get_db)) -> TodoRepository:
    return TodoRepository(db=db)


def get_todo_service(repository=Depends(get_todo_repository)) -> TodoService:
    return TodoService(repository=repository)
