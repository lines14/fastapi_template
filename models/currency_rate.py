from sqlalchemy.orm import Mapped
from sqlmodel import SQLModel, Field
from database.base.database import Database

class CurrencyRate(Database, SQLModel):
    id: int = Field(primary_key=True, nullable=False)
    rate: float = Field(nullable=False)
    currency_id: int = Field(index=True, nullable=False)

    def __init__(self, rate=None, currency_id=None):
        self.rate = rate
        self.currency_id = currency_id