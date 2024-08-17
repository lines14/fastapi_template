from sqlalchemy.sql import func
from database.database import Database
from sqlalchemy import Column, Integer, String, DateTime

class ProductGroup(Database.Base):
    __tablename__ = 'product_groups'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    group = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)