from sqlalchemy.sql import func
from database.database import Database
from sqlalchemy import Column, Integer, String, DateTime

class User(Database.Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    login = Column(String(255), nullable=False, index=True)
    host = Column(String(255), nullable=False)
    user_agent = Column(String(255), nullable=False)
    token = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), nullable=False)