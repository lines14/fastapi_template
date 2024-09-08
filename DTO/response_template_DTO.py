from typing import Any
from pydantic import Field
from DTO.base import BaseDTO
from DTO.response_template_context_DTO import ResponseTemplateContextDTO

class ResponseTemplateDTO(BaseDTO):
    status_code: int
    background: Any
    body: str
    context: ResponseTemplateContextDTO
    headers: dict = Field(default_factory=dict)