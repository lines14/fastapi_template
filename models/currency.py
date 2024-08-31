from sqlmodel import Field
from datetime import datetime
from database.base.database import Database
from models.base.base_model import BaseModel
from sqlalchemy import func, Column, func, DateTime

class Currency(BaseModel, table=True):
    __tablename__ = 'currencies'
    id: int = Field(primary_key=True, nullable=False)
    currency: str = Field(index=True, nullable=False)
    created_at: datetime = Field(sa_column=Column(DateTime, server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime, server_default=func.now(), nullable=False, onupdate=func.now()))

    async def get(model):
        async with Database() as database:
            return await database.get(model)

    async def get_all(model):
        async with Database() as database:
            return await database.get_all(model)