from sqlmodel import Field
from models.base.base_model import BaseModel

class ProductType(BaseModel, table=True):
    __tablename__ = 'product_types'
    type: str = Field(nullable=False)
    group_id: int = Field(index=True, nullable=False, foreign_key='product_groups.id')