from sqlalchemy.orm import Mapped
from database.base.database import Database

class Currency(Database):
    __tablename__ = 'currencies'

    currency: Mapped[Database.str_indexed_not_nullable]

    def __init__(self, currency=None):
        self.currency = currency

    async def get(self):
        async with Database() as database:
            return await database.get(self)

    async def get_all(self):
        async with Database() as database:
            return await database.get_all(self)