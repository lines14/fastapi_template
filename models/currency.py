from sqlalchemy.orm import Mapped
from sqlmodel import SQLModel, Field
from database.base.database import Database

class Currency(Database, SQLModel):
    __tablename__ = 'currencies'

    id: int = Field(primary_key=True, nullable=False)
    currency: str = Field(index=True, nullable=False)

    def __init__(self, currency=None):
        self.currency = currency

    async def get(self):
        async with Database() as database:
            return await database.get(self)

    async def get_all(self):
        async with Database() as database:
            return await database.get_all(self)