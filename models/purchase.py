from sqlmodel import Field
from models.base.base_model import BaseModel

class Purchase(BaseModel, table=True):
    cost: float = Field(nullable=False)
    sub_type_id: int = Field(index=True, nullable=False, foreign_key='product_sub_types.id')
    currency_id: int = Field(nullable=False, foreign_key='currencies.id')