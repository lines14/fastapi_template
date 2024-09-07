from sqlalchemy import Column, String
from models.base.base_model import BaseModel

class User(BaseModel):
    __tablename__ = 'users'
    login: str = Column(String, index=True, nullable=False)
    password: str = Column(String, nullable=False)

    def __init__(self, login=None, password=None):
        super().__init__()
        self.login = login
        self.password = password