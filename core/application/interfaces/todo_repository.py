from abc import ABC, abstractmethod
from core.domain.todo import TodoEntity


class TodoRepositoryInterface(ABC):
    @abstractmethod
    async def add_todo(self, todo: TodoEntity) -> TodoEntity:
        pass

    @abstractmethod
    async def get_todo(self, todo_id: str) -> TodoEntity | None:
        pass

    @abstractmethod
    async def get_all_todos(self) -> list[TodoEntity]:
        pass

    @abstractmethod
    async def update_todo(self, todo: TodoEntity) -> TodoEntity | None:
        pass

    @abstractmethod
    async def delete_todo(self, todo_id: str) -> bool | None:
        pass
