from DTO.base import BaseDTO
from datetime import datetime

class JWTDTO(BaseDTO):
    login: str
    exp: datetime