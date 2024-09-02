import json
from fastapi import Response
from DTO import ResponseDTO, ResponseContentDTO

class ResponseUtils:
    @staticmethod
    async def success(
        msg: str = '', 
        data: str | dict | list = '', 
        status_code: int = 202, 
        media_type="application/json"
    ) -> Response:
        content = ResponseContentDTO(
            success=True, 
            message=msg, 
            data=data
        )
        response = ResponseDTO(
            content=json.dumps(vars(content)), 
            media_type=media_type, 
            status_code=status_code
        )
        return Response(**vars(response))

    @staticmethod
    async def error(
        msg: str = '', 
        data: str | dict | list = '', 
        status_code: int = 400, 
        media_type="application/json"
    ) -> Response:
        content = ResponseContentDTO(
            success=False, 
            message=msg, 
            data=data
        )
        response = ResponseDTO(
            content=json.dumps(vars(content)), 
            media_type=media_type, 
            status_code=status_code
        )
        return Response(**vars(response))