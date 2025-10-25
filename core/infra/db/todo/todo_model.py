from ..session import Base
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid


class TodoModel(Base):
    __tablename__ = 'todos'

    id = mapped_column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    title = mapped_column(String(50), nullable=False)
    description = mapped_column(String(255))
    created_at = mapped_column(
        DateTime(timezone=True), default=func.now(), nullable=False)
    updated_at = mapped_column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = mapped_column(DateTime(timezone=True))
