import jwt
import json
import bcrypt
from os import getenv
from utils.data_utils import DataUtils
from datetime import datetime, timedelta
from utils.storage_utils import StorageUtils
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

class JWTUtils:
    @staticmethod
    def generate_token(login: int) -> str:
        payload = DataUtils.params
        payload.login = login
        payload.exp = datetime.utcnow() + timedelta(seconds=int(getenv('TTL')))
        return jwt.encode(vars(payload), StorageUtils.private_key, algorithm=getenv('ALGORITHM'))

    @classmethod
    def verify_token(cls, token: str) -> dict:
        try:
            return jwt.decode(
                token, 
                cls.__parse_public_key(StorageUtils.public_key), 
                algorithms=[getenv('ALGORITHM')]
            )
        except jwt.ExpiredSignatureError as e:
            raise jwt.ExpiredSignatureError(json.dumps(DataUtils.responses.unauthorized))
        except jwt.InvalidTokenError as e:
            raise e

    @staticmethod
    def hash_token(token: str):
        token_bytes = token.encode('utf-8')
        hashed_token = bcrypt.hashpw(token_bytes, bcrypt.gensalt())
        return hashed_token.decode('utf-8')
    
    @staticmethod
    def __parse_public_key(key_pem: str) -> serialization.load_pem_public_key:
        key_bytes = key_pem.encode()
        return serialization.load_pem_public_key(key_bytes, backend=default_backend())