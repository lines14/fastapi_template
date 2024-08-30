from sqlalchemy.orm import Mapped
from sqlmodel import SQLModel, Field
from database.base.database import Database

class User(Database, SQLModel):
    id: int | None = Field(default=None, primary_key=True, nullable=False)
    login: str = Field(index=True, nullable=False)
    password: str = Field(nullable=False)

    def __init__(self, login=None, password=None):
        self.login = login
        self.password = password

    async def create(self):
        async with Database() as database:
            await database.create(self)

    async def get(self):
        async with Database() as database:
            return await database.get(self)