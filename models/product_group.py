from sqlmodel import Field
from datetime import datetime
from models.base.base_model import BaseModel
from sqlalchemy import func, Column, func, DateTime

class ProductGroup(BaseModel, table=True):
    __tablename__ = 'product_groups'
    id: int = Field(primary_key=True, nullable=False)
    group: str = Field(nullable=False)
    created_at: datetime = Field(sa_column=Column(DateTime, server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime, server_default=func.now(), nullable=False, onupdate=func.now()))