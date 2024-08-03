from typing import Any
from fastapi import Response
    
async def send_error(msg: str, data: Any = '', status_code: int = 400) -> Response:
    content = {
        'status': False,
        'message': msg,
        'data': data
    }

    return Response(content=content, media_type="application/json", status_code=status_code)

async def send_success(msg: str, data: Any = '', status_code: int = 200) -> Response:
    content = {
        'status': True,
        'message': msg,
        'data': data
    }

    return Response(content=content, media_type="application/json", status_code=status_code)