from pydantic import Field
from DTO.base import BaseDTO

class ResponseDTO(BaseDTO):
    status_code: int
    content: str
    media_type: str
    headers: dict = Field(default_factory=dict)