from sqlalchemy.sql import func
from database.database import Database
from sqlalchemy import Column, Integer, String, DateTime

class ProductType(Database.Base):
    __tablename__ = 'product_types'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    type = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)