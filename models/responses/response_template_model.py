from typing import Any
from pydantic import Field
from models.base.base_model import BaseModel
from models.responses.response_template_context_model import ResponseTemplateContextModel

class ResponseTemplateModel(BaseModel):
    status_code: int
    background: Any
    body: str
    context: ResponseTemplateContextModel
    headers: dict = Field(default_factory=dict)