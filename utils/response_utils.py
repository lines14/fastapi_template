import json
from typing import Any
from fastapi import Response

class ResponseUtils:
    @staticmethod
    async def success(msg: str, data: Any = '', status_code: int = 200) -> Response:
        content = type('', (object,), {})()
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
        content = type('', (object,), {})()
        content.status = False
        content.message = msg
        content.data = data

        return Response(
            content=json.dumps(vars(content)), 
            media_type="application/json", 
            status_code=status_code
        )