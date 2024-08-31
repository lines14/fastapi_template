import json
from fastapi import Response
from models.responses.response_model import ResponseModel
from models.responses.response_content_model import ResponseContentModel

class ResponseUtils:
    @staticmethod
    async def success(
        msg: str = '', 
        data: str | dict | list = '', 
        status_code: int = 200, 
        media_type="application/json"
    ) -> Response:
        content = ResponseContentModel(success=True, message=msg, data=data)
        response = ResponseModel(
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
        content = ResponseContentModel(success=False, message=msg, data=data)
        response = ResponseModel(
            content=json.dumps(vars(content)), 
            media_type=media_type, 
            status_code=status_code
        )
        return Response(**vars(response))