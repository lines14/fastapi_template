from sqlmodel import Field
from models.base.base_model import BaseModel

class Currency(BaseModel, table=True):
    __tablename__ = 'currencies'
    currency: str = Field(nullable=False)