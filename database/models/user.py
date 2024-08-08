from sqlalchemy.sql import func
from database.base_db import BaseDB
from sqlalchemy import Column, Integer, String, DateTime

base_DB = BaseDB()

class User(base_DB.Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)