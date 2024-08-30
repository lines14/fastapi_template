from pydantic import BaseModel

class ProductGroup(BaseModel):
    id = int
    group = str
    created_at = str
    updated_at = str