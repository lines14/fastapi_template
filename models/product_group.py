from sqlalchemy.orm import Mapped
from database.base.database import Database

class ProductGroup(Database):
    group: Mapped[Database.str_not_nullable]

    def __init__(self, group=None):
        self.group = group

    async def get(self):
        async with Database() as database:
            return await database.get(self)