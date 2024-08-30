from sqlalchemy.sql import func
from database.base.database import Database
from sqlalchemy import Column, Integer, String, DateTime

class Session(Database):
    __tablename__ = 'sessions'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    login = Column(String(255), nullable=False, index=True)
    host = Column(String(255), nullable=False)
    user_agent = Column(String(255), nullable=False)
    token = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), nullable=False)

    def __init__(self, login=None, host=None, user_agent=None, token=None):
        self.db = Database()
        self.login = login
        self.host = host
        self.user_agent = user_agent
        self.token = token

    def create(self):
        self.db.create(self)

    def get(self):
        return self.db.get(self)