from fastapi import Request
from DTO.base.base_DTO import BaseDTO

class ResponseTemplateContextDTO(BaseDTO):
    request: Request
    pythonVersion: str
    fastapiVersion: str