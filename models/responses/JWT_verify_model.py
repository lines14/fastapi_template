from models.base.base_model import BaseModel

class JWTVerifyModel(BaseModel):
    login: str
    exp: int