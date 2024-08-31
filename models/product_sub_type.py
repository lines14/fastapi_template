from sqlmodel import Field
from datetime import datetime
from models.base.base_model import BaseModel
from sqlalchemy import func, Column, func, DateTime

class ProductSubType(BaseModel, table=True):
    __tablename__ = 'product_sub_types'
    id: int = Field(primary_key=True, nullable=False)
    sub_type: str = Field(nullable=False)
    type_id: int = Field(index=True, nullable=False)
    created_at: datetime = Field(sa_column=Column(DateTime, server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime, server_default=func.now(), nullable=False, onupdate=func.now()))