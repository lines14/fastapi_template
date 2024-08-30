from sqlalchemy.orm import Mapped
from sqlmodel import SQLModel, Field
from database.base.database import Database

class ProductType(Database, SQLModel):
    id: int = Field(primary_key=True, nullable=False)
    type: str = Field(nullable=False)
    group_id: int = Field(index=True, nullable=False)

    def __init__(self, type=None, group_id=None):
        self.type = type
        self.group_id = group_id

    async def get(self):
        async with Database() as database:
            return await database.get(self)