import jwt
import json
import bcrypt
import datetime
from os import getenv
from utils.data_utils import DataUtils
from utils.storage_utils import StorageUtils
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

ALGORITHM = 'RS256'
with open(StorageUtils.get_JWT('private.pem')) as file:
    PRIVATE_KEY = file.read()
with open(StorageUtils.get_JWT('public.pem')) as file:
    PUBLIC_KEY = file.read()

class JWTUtils:
    @staticmethod
    def generate_token(login: int) -> str:
        payload = {
            'login': login,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=int(getenv('TTL')))
        }

        token = jwt.encode(payload, PRIVATE_KEY, algorithm=ALGORITHM)
        return token

    @classmethod
    def verify_token(cls, token: str) -> dict:
        try:
            payload = jwt.decode(token, cls.__parse_public_key(PUBLIC_KEY), algorithms=[ALGORITHM])
            return payload
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
        key = serialization.load_pem_public_key(key_bytes, backend=default_backend())
        return key