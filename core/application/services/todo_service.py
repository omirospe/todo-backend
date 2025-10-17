from ..dtos.todo_dtos import TodoDTO


class TodoService:

    def __init__(self, text: str):
        self.text = text

    async def create_todo(self, dto: TodoDTO) -> TodoDTO:
        dto.id = '1'
        print(self.text)
        return dto

    async def get_todo(self, todo_id: str) -> TodoDTO:
        pass

    async def get_all_todos(self) -> list[TodoDTO]:
        pass

    async def update_todo(self, todo_id: str) -> TodoDTO:
        pass

    async def delete_todo(self, todo_id: str):
        pass
