from pydantic import BaseModel

class Session(BaseModel):
    id = int
    login = str
    host = str
    user_agent = str
    token = str
    created_at = str
    updated_at = str