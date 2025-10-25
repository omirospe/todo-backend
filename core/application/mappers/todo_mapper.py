from ..dtos import TodoDTO
from core.domain.todo import TodoEntity

class TodoDTOMapper:

    @staticmethod
    def entity_to_dto(entity: TodoEntity) -> TodoDTO:
        dto = TodoDTO()

        dto.id = entity.id
        dto.title = entity.title
        dto.description = entity.description
        dto.created_at = entity.created_at
        dto.updated_at = entity.updated_at
        dto.deleted_at = entity.deleted_at

        return dto

    @staticmethod
    def dto_to_entity(dto: TodoDTO) -> TodoEntity:
        return TodoEntity(
            id=str(dto.id) if dto.id else None,
            title=dto.title,
            description=dto.description,
            created_at=dto.created_at,
            updated_at=dto.updated_at,
            deleted_at=dto.deleted_at,
        )

    @staticmethod
    def entities_to_dtos(entities: list[TodoEntity]) -> list[TodoDTO]:
        return [TodoDTOMapper.entity_to_dto(entity) for entity in entities]
