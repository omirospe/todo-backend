from fastapi import APIRouter
from .todo_router import router as todo_router


protected_router = APIRouter(prefix="/api/v1")

protected_router.include_router(todo_router)
