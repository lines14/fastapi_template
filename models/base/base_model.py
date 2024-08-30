from sqlmodel import SQLModel

class BaseModel(SQLModel):
    class Config:
        validate_assignment = True