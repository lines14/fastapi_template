from sqlmodel import Field
from models.base.base_model import BaseModel

class BankAccountIssuer(BaseModel, table=True):
    issuer: str = Field(nullable=False)
    country_code: str = Field(nullable=False)