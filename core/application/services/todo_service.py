from ..dtos.todo_dtos import TodoDTO
from ..interfaces import TodoRepositoryInterface
from ..mappers import TodoDTOMapper


class TodoService:

    def __init__(self, repository: TodoRepositoryInterface):
        self.repository = repository

    async def create_todo(self, dto: TodoDTO) -> TodoDTO:
        todo = TodoDTOMapper.dto_to_entity(dto)
        created_todo = await self.repository.add_todo(todo)

        return TodoDTOMapper.entity_to_dto(created_todo)

    async def get_todo(self, todo_id: str) -> TodoDTO:
        todo = await self.repository.get_todo(todo_id)

        if not todo:
            raise Exception('Todo not found')

        return TodoDTOMapper.entity_to_dto(todo)

    async def get_all_todos(self) -> list[TodoDTO]:
        todos = await self.repository.get_all_todos()

        return TodoDTOMapper.entities_to_dtos(todos)

    async def update_todo(self, dto: TodoDTO) -> TodoDTO:
        todo = await self.repository.get_todo(dto.id)
        todo.update_description(dto.description)
        updated_todo = await self.repository.update_todo(todo)

        return TodoDTOMapper.entity_to_dto(updated_todo)

    async def delete_todo(self, todo_id: str) -> bool:
        response = await self.repository.delete_todo(todo_id)

        if not response:
            raise Exception('Todo not found')

        return True
