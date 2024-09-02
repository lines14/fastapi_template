from DTO.base.base_DTO import BaseDTO

class JWTVerifyDTO(BaseDTO):
    login: str
    exp: int