from sqlmodel import Field
from models.base.base_model import BaseModel

class CurrencyRate(BaseModel, table=True):
    rate: float = Field(nullable=False)
    currency_id: int = Field(index=True, nullable=False, foreign_key='currencies.id')