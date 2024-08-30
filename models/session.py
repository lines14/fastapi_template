from sqlalchemy.orm import Mapped
from database.base.database import Database

class Session(Database):
    login: Mapped[Database.str_indexed_not_nullable]
    host: Mapped[Database.str_not_nullable]
    user_agent: Mapped[Database.str_not_nullable]
    token: Mapped[Database.str_not_nullable]

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