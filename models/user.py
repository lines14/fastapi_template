from sqlmodel import SQLModel
from sqlalchemy.orm import Mapped
from database.base.database import Database

class User(Database, SQLModel):
    login: Mapped[Database.str_indexed_not_nullable]
    password: Mapped[Database.str_not_nullable]

    def __init__(self, login=None, password=None):
        self.login = login
        self.password = password

    async def create(self):
        async with Database() as database:
            await database.create(self)

    async def get(self):
        async with Database() as database:
            return await database.get(self)