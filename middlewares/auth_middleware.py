import json
from DTO import JWTDTO
from models import Session
from functools import wraps
from typing import Callable, Any
from utils.JWT_utils import JWTUtils
from fastapi import Request, Response
from utils.data_utils import DataUtils
from utils.response_utils import ResponseUtils
from utils.cryptography_utils import CryptographyUtils
from repositories.redis_repository import RedisRepository

class AuthMiddleware:
    def check_bearer_token(self, function: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(function)
        async def wrapper(request: Request, *args: Any, **kwargs: Any) -> Response:
            auth_header = request.headers.get('Authorization')
            if auth_header and auth_header.startswith('Bearer '):
                try:
                    request_token = auth_header.split(" ")[1]
                    payload = JWTDTO(**JWTUtils.verify_token(request_token))
                    user = await Session(login=payload.login).get()
                    saved_token = await RedisRepository().get_user(payload.login)
                    if (user and CryptographyUtils.verify_string(request_token, user.token) 
                        and request_token == saved_token.decode('utf-8')):
                        return await function(request, *args, **kwargs)
                    else:
                        return await ResponseUtils.error(*DataUtils.responses.unauthorized)
                except Exception as e:
                    try:
                        error_response = json.loads(str(e))
                        return await ResponseUtils.error(*error_response)
                    except:
                        return await ResponseUtils.error(str(e))
            else:
                return await ResponseUtils.error(*DataUtils.responses.unauthorized)
        return wrapper