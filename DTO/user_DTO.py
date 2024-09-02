from DTO.base.base_DTO import BaseDTO
from DTO.base.rules import Login, Password

class UserDTO(BaseDTO):
    login: Login
    password: Password