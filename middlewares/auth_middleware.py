from functools import wraps
from typing import Callable, Any
from utils.JWT_utils import JWTUtils
from fastapi import Request, Response
from utils.response_utils import ResponseUtils
from repositories.redis_repository import RedisRepository

class AuthMiddleware:
    def bearer_token(self, function: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(function)
        async def wrapper(request: Request, *args: Any, **kwargs: Any) -> Response:
            auth = request.headers.get('Authorization')
            if auth and auth.startswith('Bearer '):
                token = auth.split(" ")[1]
                try:
                    payload = JWTUtils.verify_token(token)
                    redis_repository = RedisRepository()
                    savedToken = redis_repository.get_user(payload['login'])
                    if token == savedToken:
                        return await function(request, *args, **kwargs)
                    else:
                        return await ResponseUtils.error('Unauthorized', '', 401)
                except Exception as e:
                    return await ResponseUtils.error(str(e))
            else:
                return await ResponseUtils.error('Unauthorized', '', 401)
        return wrapper