from pydantic import StrictBool
from DTO.base.base_DTO import BaseDTO

class ResponseContentDTO(BaseDTO):
    success: StrictBool
    message: str
    data: str | dict | list