from sqlalchemy.sql import func
from database.base.database import Database
from sqlalchemy import Column, Integer, String, DateTime

class User(Database):
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    login = Column(String(255), nullable=False, index=True)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), nullable=False)

    def __init__(self, login=None, password=None):
        self.login = login
        self.password = password

    async def create(self):
        async with Database() as database:
            await database.create(self)

    async def get(self):
        async with Database() as database:
            return await database.get(self)