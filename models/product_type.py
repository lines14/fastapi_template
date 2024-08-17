from sqlalchemy.sql import func
from database.database import Database
from sqlalchemy import Column, Integer, String, DateTime

class ProductType(Database.Base):
    __tablename__ = 'product_types'
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(255), nullable=False, index=True)