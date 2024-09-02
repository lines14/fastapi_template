from datetime import datetime
from DTO.base.base_DTO import BaseDTO

class JWTDTO(BaseDTO):
    login: str
    exp: datetime