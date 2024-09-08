import jwt
import json
from os import getenv
from DTO import JWTDTO
from utils.data_utils import DataUtils
from datetime import datetime, timedelta
from utils.storage_utils import StorageUtils
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

class JWTUtils:
    @staticmethod
    def generate_token(login: str) -> str:
        payload = JWTDTO(
            login=login, 
            exp=datetime.utcnow() + timedelta(seconds=int(getenv('TOKEN_TTL')))
        )
        return jwt.encode(
            vars(payload), 
            StorageUtils.private_key, 
            algorithm=getenv('ENCODE_ALGORITHM')
        )

    @classmethod
    def verify_token(cls, token: str) -> dict:
        try:
            return jwt.decode(
                token, 
                cls.__parse_public_key(StorageUtils.public_key), 
                algorithms=[getenv('ENCODE_ALGORITHM')]
            )
        except jwt.ExpiredSignatureError as e:
            raise jwt.ExpiredSignatureError(json.dumps(DataUtils.responses.unauthorized_error))
        except jwt.InvalidTokenError as e:
            raise e
    
    @staticmethod
    def __parse_public_key(key_pem: str) -> serialization.load_pem_public_key:
        key_bytes = key_pem.encode()
        return serialization.load_pem_public_key(key_bytes, backend=default_backend())