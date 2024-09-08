import json
from typing import Union
from fastapi import Response
from DTO import ResponseDTO, ResponseContentDTO

class ResponseUtils:
    @staticmethod
    async def success(
        msg: str = '', 
        data: Union[str, dict, list] = '', 
        status_code: int = 200, 
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
        data: Union[str, dict, list] = '', 
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