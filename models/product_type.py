from sqlmodel import Field
from datetime import datetime
from models.base.base_model import BaseModel
from sqlalchemy import func, Column, DateTime

class ProductType(BaseModel, table=True):
    __tablename__ = 'product_types'
    id: int = Field(primary_key=True, nullable=False)
    type: str = Field(nullable=False)
    group_id: int = Field(index=True, nullable=False, foreign_key='product_groups.id')
    created_at: datetime = Field(sa_column=Column(DateTime, server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime, server_default=func.now(), nullable=False, onupdate=func.now()))