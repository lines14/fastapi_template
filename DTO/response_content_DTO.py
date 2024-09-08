from typing import Union
from DTO.base import BaseDTO
from pydantic import StrictBool

class ResponseContentDTO(BaseDTO):
    success: StrictBool
    message: str
    data: Union[str, dict, list]