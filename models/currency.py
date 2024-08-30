from pydantic import BaseModel

class Currency(BaseModel):
    id = int
    currency = str
    created_at = str
    updated_at = str