import json
from typing import Any
from fastapi import Response
from utils.data_utils import DataUtils

class ResponseUtils:
    @staticmethod
    async def success(msg: str, data: Any = '', status_code: int = 200) -> Response:
        content = DataUtils.obj_template
        content.status = True
        content.message = msg
        content.data = data

        return Response(
            content=json.dumps(vars(content)), 
            media_type="application/json", 
            status_code=status_code
        )

    @staticmethod
    async def error(msg: str, data: Any = '', status_code: int = 400) -> Response:
        content = DataUtils.obj_template
        content.status = False
        content.message = msg
        content.data = data

        return Response(
            content=json.dumps(vars(content)), 
            media_type="application/json", 
            status_code=status_code
        )