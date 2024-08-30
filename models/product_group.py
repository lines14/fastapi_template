from sqlalchemy.orm import Mapped
from sqlmodel import SQLModel, Field
from database.base.database import Database

class ProductGroup(Database, SQLModel):
    id: int = Field(primary_key=True, nullable=False)
    group: str = Field(nullable=False)

    def __init__(self, group=None):
        self.group = group

    async def get(self):
        async with Database() as database:
            return await database.get(self)