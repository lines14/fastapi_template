from sqlalchemy.orm import Mapped
from database.base.database import Database

class ProductType(Database):
    type: Mapped[Database.str_not_nullable]
    group_id: Mapped[Database.int_indexed_not_nullable]

    def __init__(self, type=None, group_id=None):
        self.type = type
        self.group_id = group_id

    async def get(self):
        async with Database() as database:
            return await database.get(self)