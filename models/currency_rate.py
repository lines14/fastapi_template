from sqlmodel import Field
from datetime import datetime
from models.base.base_model import BaseModel
from sqlalchemy import func, Column, DateTime

class CurrencyRate(BaseModel, table=True):
    __tablename__ = 'currency_rates'
    id: int = Field(primary_key=True, nullable=False)
    rate: float = Field(nullable=False)
    currency_id: int = Field(index=True, nullable=False, foreign_key='currencies.id')
    created_at: datetime = Field(sa_column=Column(DateTime, server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime, server_default=func.now(), nullable=False, onupdate=func.now()))