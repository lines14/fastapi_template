from pydantic import BaseModel

class ProductType(BaseModel):
    id = int
    type = str
    group_id = int
    created_at = str
    updated_at = str