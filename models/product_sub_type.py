from sqlmodel import Field
from models.base.base_model import BaseModel

class ProductSubType(BaseModel, table=True):
    sub_type: str = Field(nullable=False)
    type_id: int = Field(index=True, nullable=False, foreign_key='product_types.id')