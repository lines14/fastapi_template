from repositories.redis import RedisRepository
from typing import Callable, Any
from flask import request, Response, g
from utils.jwt import verify_token
from utils.responses import send_error

redis_repository = RedisRepository()

def bearer_token(f: Callable[..., Any]) -> Callable[..., Any]:
    def wrap(*args: Any, **kwargs: Any) -> Response:
        auth = request.headers.get('Authorization')
        if auth and auth.startswith('Bearer '):
            token = auth.split(" ")[1]
            try:
                payload = verify_token(token)
                user = redis_repository.get_user(payload['sub'])
                g.user = user
                return f(*args, **kwargs)
            except:
                return send_error('Invalid token', '', 401)
        else:
            return send_error('Unauthorized', '', 401)
    wrap.__name__ = f.__name__
    return wrap