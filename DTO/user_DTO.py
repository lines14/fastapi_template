from DTO.base.base_DTO import BaseDTO
from utils.data_utils import DataUtils
from pydantic import Field, model_validator

class UserDTO(BaseDTO):
    login: str = Field(
        default=..., 
        description='Должен содержать только буквы и цифры и не должен содержать пробелов', 
        min_length=4, 
        max_length=20
    )
    password: str = Field(
        default=..., 
        description='Должен содержать только буквы и цифры и не должен содержать пробелов', 
        min_length=6, 
        max_length=20
    )

    @model_validator(mode="after")
    @classmethod
    def validate_fields(cls, values):
        login = values.login
        password = values.password
        if len(login) < 4 or len(login) > 20 or not login.isalnum() or ' ' in login:
            raise ValueError(DataUtils.responses.login_validation_error)
        if len(password) < 6 or len(password) > 20 or not password.isalnum() or ' ' in password:
            raise ValueError(DataUtils.responses.password_validation_error)
        return values