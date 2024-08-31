from pydantic import StrictBool
from models.base.base_model import BaseModel

class ResponseContentModel(BaseModel):
    success: StrictBool
    message: str
    data: str | dict | list