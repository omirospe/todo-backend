from ..shared import BaseORMMapper
from core.infra.db.todo import TodoModel
from core.domain.todo import TodoEntity


class TodoORMMapper(BaseORMMapper):
    @staticmethod
    def orm_to_entity(orm: TodoModel) -> TodoEntity:
        return TodoEntity(
            id=str(orm.id),
            title=orm.title,
            description=orm.description,
            created_at=orm.created_at,
            updated_at=orm.updated_at,
            deleted_at=orm.deleted_at,
        )

    @staticmethod
    def entity_to_orm(entity: TodoEntity) -> TodoModel:
        orm = TodoModel()
        if entity.id:
            orm.id = str(entity.id)
            
        orm.title = entity.title
        orm.description = entity.description
        orm.deleted_at = str(entity.deleted_at) if entity.deleted_at else None
        return orm

    @staticmethod
    def orms_to_entities(orms: list[TodoModel]) -> list[TodoEntity]:
        return [TodoORMMapper.orm_to_entity(orm) for orm in orms]
