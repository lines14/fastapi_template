from sqlmodel import Field
from datetime import datetime
from database.base.database import Database
from models.base.base_model import BaseModel
from sqlalchemy import func, Column, DateTime
from models.base.extended_types import Login, Password

class User(BaseModel, table=True):
    __tablename__ = 'users'
    id: int = Field(primary_key=True, nullable=False)
    login: Login = Field(index=True, nullable=False)
    password: Password = Field(nullable=False)
    created_at: datetime = Field(sa_column=Column(DateTime, server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime, server_default=func.now(), nullable=False, onupdate=func.now()))

    async def create(self):
        async with Database() as database:
            await database.create(self)

    async def get(self):
        async with Database() as database:
            return await database.get(self)