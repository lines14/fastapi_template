from sqlalchemy.sql import func
from database.base.database import Database
from sqlalchemy import Column, Integer, Float, DateTime

class CurrencyRate(Database.Base):
    __tablename__ = 'currency_rates'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    rate = Column(Float, nullable=False)
    currency_id = Column(Integer, index=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), nullable=False)