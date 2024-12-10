from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime


class User(SQLModel, table=True):
    id: str = Field(
        ..., primary_key=True, index=True, max_length=33,
        schema_extra={'pattern': r"^U[a-f0-9]{32}$"}
    )
    thread_id: str = Field(
        ..., max_length=45, schema_extra={'pattern': r"^thread_"}
    )
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    updated_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(),
        sa_column_kwargs={"onupdate": lambda: datetime.now()}
    )
"""
    artifacts: List["Artifact"] = Relationship(back_populates="user")
"""
