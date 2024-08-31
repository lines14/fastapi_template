from pydantic import Field
from models.base.base_model import BaseModel
from models.responses.response_content_model import ResponseContentModel

class ResponseModel(BaseModel):
    status_code: int
    content: str
    media_type: str
    headers: dict = Field(default_factory=dict)