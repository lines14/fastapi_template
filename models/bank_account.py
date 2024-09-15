from sqlmodel import Field
from models.base.base_model import BaseModel

class BankAccount(BaseModel, table=True):
    account: str = Field(nullable=False)
    issuer_id: int = Field(nullable=False, foreign_key='bank_account_issuers.id')
    currency_id: int = Field(index=True, nullable=False, foreign_key='currencies.id')
    user_id: int = Field(index=True, nullable=False, foreign_key='users.id')