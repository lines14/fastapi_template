from pydantic import BaseModel

class CurrencyRate(BaseModel):
    id = int
    rate = float
    currency_id = int
    created_at = str
    updated_at = str