from fastapi import APIRouter, status, Depends
from core.application.services.todo_service import TodoService
from ..mappers.todo_api_mapper import TodoAPIMapper
from ..dependencies.todo_dependency import get_todo_service
from ..schemas.todo_schemas import (
    CreateTodoSchema,
    UpdatedTodoSchema,
    TodoResponseSchema,
    TodoListItemResponseSchema
)

router = APIRouter()


@router.post(
    '/',
    response_model=TodoResponseSchema,
    status_code=status.HTTP_201_CREATED
)
async def create_todo(
    schema: CreateTodoSchema,
    service: TodoService = Depends(get_todo_service)
):
    dto = TodoAPIMapper.from_create_schema(schema)
    response = await service.create_todo(dto)
    return response


@router.get('/all', response_model=list[TodoListItemResponseSchema])
async def get_all_todos(
    service: TodoService = Depends(get_todo_service)
):
    response = await service.get_all_todos()
    return response


@router.get('/{todo_id}', response_model=TodoResponseSchema)
async def get_todo(
    todo_id: str = None,
    service: TodoService = Depends(get_todo_service)
):
    response = await service.get_todo(todo_id)
    return response


@router.put('/{todo_id}', response_model=TodoResponseSchema)
async def update_todo(
    todo_id: str = None,
    schema: UpdatedTodoSchema = None,
    service: TodoService = Depends(get_todo_service)
):
    dto = TodoAPIMapper.from_create_schema(schema)
    dto.id = todo_id
    response = await service.update_todo(dto)
    return response


@router.delete(
    '/{todo_id}',
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_todo(
    todo_id: str = None,
    service: TodoService = Depends(get_todo_service)
):
    response = await service.delete_todo(todo_id)
    return response
