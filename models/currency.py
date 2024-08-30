from datetime import datetime
from sqlmodel import SQLModel, Field
from database.base.database import Database
from sqlalchemy import func, Column, func, DateTime

class Currency(SQLModel):
    __tablename__ = 'currencies'

    id: int = Field(primary_key=True, nullable=False)
    created_at: datetime = Field(sa_column=Column(DateTime, server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime, server_default=func.now(), nullable=False, onupdate=datetime.now))
    currency: str = Field(index=True, nullable=False)

    def __init__(self, currency=None):
        self.currency = currency

    async def get(self):
        async with Database() as database:
            return await database.get(self)

    async def get_all(self):
        async with Database() as database:
            return await database.get_all(self)