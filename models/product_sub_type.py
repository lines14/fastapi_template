from datetime import datetime
from sqlmodel import SQLModel, Field
from sqlalchemy import func, Column, func, DateTime

class ProductSubType(SQLModel):
    id: int = Field(primary_key=True, nullable=False)
    created_at: datetime = Field(sa_column=Column(DateTime, server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime, server_default=func.now(), nullable=False, onupdate=datetime.now))
    sub_type: str = Field(nullable=False)
    type_id: int = Field(index=True, nullable=False)

    def __init__(self, sub_type=None, type_id=None):
        self.sub_type = sub_type
        self.type_id = type_id