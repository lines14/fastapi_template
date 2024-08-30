from datetime import datetime
from sqlmodel import SQLModel, Field
from database.base.database import Database
from sqlalchemy import func, Column, func, DateTime

class Session(SQLModel):
    id: int = Field(primary_key=True, nullable=False)
    created_at: datetime = Field(sa_column=Column(DateTime, server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime, server_default=func.now(), nullable=False, onupdate=datetime.now))
    login: str = Field(index=True, nullable=False)
    host: str = Field(nullable=False)
    user_agent: str = Field(nullable=False)
    token: str = Field(nullable=False)

    def __init__(self, login=None, host=None, user_agent=None, token=None):
        self.login = login
        self.host = host
        self.user_agent = user_agent
        self.token = token

    async def create(self):
        async with Database() as database:
            await database.create(self)

    async def get(self):
        async with Database() as database:
            return await database.get(self)