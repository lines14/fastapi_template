from sqlalchemy import Column, String
from models.base.base_model import BaseModel

class Currency(BaseModel):
    __tablename__ = 'currencies'
    currency = Column(String, index=True, nullable=False)

    def __init__(self, currency=None):
        super().__init__()
        self.currency = currency