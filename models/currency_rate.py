from models.base.base_model import BaseModel
from sqlalchemy import Column, Integer, Float, ForeignKey

class CurrencyRate(BaseModel):
    __tablename__ = 'currency_rates'
    rate = Column(Float, nullable=False)
    currency_id = Column(Integer, ForeignKey('currencies.id'), index=True, nullable=False)

    def __init__(self, rate=None, currency_id=None):
        super().__init__()
        self.rate = rate
        self.currency_id = currency_id