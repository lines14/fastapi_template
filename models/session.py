from sqlalchemy import Column, String
from models.base.base_model import BaseModel

class Session(BaseModel):
    __tablename__ = 'sessions'
    login: str = Column(String, index=True, nullable=False)
    host: str = Column(String, nullable=False)
    user_agent: str = Column(String, nullable=False)
    token: str = Column(String, nullable=False)

    def __init__(self, login=None, token=None, host=None, user_agent=None):
        super().__init__()
        self.login = login
        self.token = token
        self.host = host
        self.user_agent = user_agent