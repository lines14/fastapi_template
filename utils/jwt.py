import jwt
from utils.paths import storage_path
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

with open(storage_path('jwt/public.pem')) as file:
    secret_file = file.read()

ALGORITHM = 'RS256'
SECRET_KEY = secret_file

def verify_token(token: str) -> dict:
    payload = jwt.decode(token, _parse_public_key(SECRET_KEY), algorithms=[ALGORITHM])
    return payload

def _parse_public_key(key_pem: str) -> serialization.load_pem_public_key:
    key_bytes = key_pem.encode()
    key = serialization.load_pem_public_key(key_bytes, backend=default_backend())
    return key