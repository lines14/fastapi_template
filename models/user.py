from pydantic import BaseModel

class User(BaseModel):
    id = int
    login = str
    password = str
    created_at = str
    updated_at = str