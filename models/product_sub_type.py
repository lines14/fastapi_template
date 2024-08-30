from pydantic import BaseModel

class ProductSubType(BaseModel):
    id = int
    sub_type = str
    type_id = int
    created_at = str
    updated_at = str