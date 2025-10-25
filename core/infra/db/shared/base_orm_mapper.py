from abc import ABC, abstractmethod
from typing import Any


class BaseORMMapper(ABC):
    @abstractmethod
    def orm_to_entity(orm: Any) -> Any:
        pass

    @abstractmethod
    def entity_to_orm(entity: Any) -> Any:
        pass

    @abstractmethod
    def orms_to_entities(entity: list[Any]) -> list[Any]:
        pass
