from sqlalchemy.orm import Mapped
from sqlmodel import SQLModel, Field
from database.base.database import Database

class ProductSubType(Database, SQLModel):
    id: int = Field(primary_key=True, nullable=False)
    sub_type: str = Field(nullable=False)
    type_id: int = Field(index=True, nullable=False)

    def __init__(self, sub_type=None, type_id=None):
        self.sub_type = sub_type
        self.type_id = type_id