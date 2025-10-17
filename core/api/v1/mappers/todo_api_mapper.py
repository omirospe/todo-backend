from ..schemas.todo_schemas import CreateTodoSchema, UpdatedTodoSchema
from core.application.dtos.todo_dtos import TodoDTO


class TodoAPIMapper:
    @staticmethod
    def from_create_schema(schema: CreateTodoSchema) -> TodoDTO:
        return TodoDTO(
            title=schema.title,
            description=schema.description
        )

    @staticmethod
    def from_update_schema(schema: UpdatedTodoSchema) -> TodoDTO:
        return TodoDTO(
            description=schema.description
        )
