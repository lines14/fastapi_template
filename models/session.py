from sqlmodel import Field
from datetime import datetime
from database.base.database import Database
from models.base.base_model import BaseModel
from sqlalchemy import func, Column, func, DateTime

class Session(BaseModel, table=True):
    __tablename__ = 'sessions'
    id: int = Field(primary_key=True, nullable=False)
    created_at: datetime = Field(sa_column=Column(DateTime, server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime, server_default=func.now(), nullable=False, onupdate=datetime.now))
    login: str = Field(index=True, nullable=False)
    host: str = Field(nullable=False)
    user_agent: str = Field(nullable=False)
    token: str = Field(nullable=False)

    async def create(model):
        async with Database() as database:
            await database.create(model)

    async def get(model):
        async with Database() as database:
            return await database.get(model)