from fastapi import Request
from DTO.base import BaseDTO

class ResponseTemplateContextDTO(BaseDTO):
    request: Request
    pythonVersion: str
    fastapiVersion: str