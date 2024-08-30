from datetime import datetime
from sqlmodel import SQLModel, Field
from sqlalchemy import func, Column, func, DateTime

class CurrencyRate(SQLModel):
    id: int = Field(primary_key=True, nullable=False)
    created_at: datetime = Field(sa_column=Column(DateTime, server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime, server_default=func.now(), nullable=False, onupdate=datetime.now))
    rate: float = Field(nullable=False)
    currency_id: int = Field(index=True, nullable=False)

    def __init__(self, rate=None, currency_id=None):
        self.rate = rate
        self.currency_id = currency_id