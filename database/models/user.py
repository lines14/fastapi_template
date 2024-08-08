from sqlalchemy.sql import func
from database.base.base_db import Base
from sqlalchemy import Column, Integer, String, DateTime

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(255), nullable=False, index=True)
    token = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)