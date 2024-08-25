from sqlalchemy.sql import func
from database.database import Database
from sqlalchemy import Column, Integer, String, DateTime

class ProductSubType(Database.Base):
    __tablename__ = 'product_sub_types'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    sub_type = Column(String(255), nullable=False)
    type_id = Column(Integer, index=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), nullable=False)