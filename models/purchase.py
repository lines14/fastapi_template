from sqlmodel import Field
from models.base.base_model import BaseModel

class Purchase(BaseModel, table=True):
    cost: float = Field(nullable=False)
    account_id: int = Field(index=True, nullable=False, foreign_key='bank_accounts.id')
    sub_type_id: int = Field(index=True, nullable=False, foreign_key='product_sub_types.id')