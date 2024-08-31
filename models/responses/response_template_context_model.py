from fastapi import Request
from models.base.base_model import BaseModel

class ResponseTemplateContextModel(BaseModel):
    request: Request
    pythonVersion: str
    fastapiVersion: str