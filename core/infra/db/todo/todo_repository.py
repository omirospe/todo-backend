from core.application.interfaces import TodoRepositoryInterface
from core.domain.todo import TodoEntity
from .todo_mapper import TodoORMMapper
from .todo_model import TodoModel
from sqlalchemy.orm import Session


class TodoRepository(TodoRepositoryInterface):

    def __init__(self, db: Session):
        self.db = db

    async def add_todo(self, todo: TodoEntity) -> TodoEntity:
        model = TodoORMMapper.entity_to_orm(todo)
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)

        return TodoORMMapper.orm_to_entity(model)

    async def _get_todo_by_id(self, todo_id: str) -> TodoModel | None:
        q = self.db.query(TodoModel).filter(
            TodoModel.id == todo_id
        )

        return q.first()

    async def get_todo(self, todo_id: str) -> TodoEntity | None:
        model = await self._get_todo_by_id(todo_id)

        return TodoORMMapper.orm_to_entity(model) if model else None

    async def get_all_todos(self) -> list[TodoEntity]:
        q = self.db.query(TodoModel)

        models = q.all()

        return TodoORMMapper.orms_to_entities(models)

    async def update_todo(self, todo: TodoEntity) -> TodoEntity | None:
        model = await self._get_todo_by_id(todo.id)

        if not model:
            return None

        model.description = todo.description
        self.db.commit()
        self.db.refresh(model)

        return TodoORMMapper.orm_to_entity(model)

    async def delete_todo(self, todo_id: str) -> bool | None:
        model = await self._get_todo_by_id(todo_id)

        if not model:
            return None

        self.db.delete(model)
        self.db.commit()

        return True
