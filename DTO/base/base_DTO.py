from pydantic import BaseModel

class BaseDTO(BaseModel):
    class Config:
        orm_mode = True
        validate_assignment = True
        arbitrary_types_allowed=True