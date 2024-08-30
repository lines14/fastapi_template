from sqlalchemy.sql import func
from database.base.database import Database
from sqlalchemy import Column, Integer, String, DateTime

class Currency(Database):
    __tablename__ = 'currencies'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    currency = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), nullable=False)

    def __init__(self, currency=None):
        self.currency = currency

    async def get(self):
        async with Database() as database:
            return await database.get(self)

    async def get_all(self):
        async with Database() as database:
            return await database.get_all(self)