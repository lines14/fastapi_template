import json
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
            auth = request.headers.get('Authorization')
            if auth and auth.startswith('Bearer '):
                token = auth.split(" ")[1]
                try:
                    payload = JWTUtils.verify_token(token)
                    redis_repository = RedisRepository()
                    savedToken = redis_repository.get_user(payload['login'])
                    user = Session(login=payload['login']).get()
                    if savedToken and user and token == savedToken.decode('utf-8') and CryptographyUtils.verify_string(token, user.token):
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