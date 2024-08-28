import bcrypt

class CryptographyUtils:
    @staticmethod
    def hash_string(token: str):
        token_bytes = token.encode('utf-8')
        hashed_token = bcrypt.hashpw(token_bytes, bcrypt.gensalt())
        return hashed_token.decode('utf-8')
    
    @staticmethod
    def verify_string(token: str, hashed_token: str) -> bool:
        token_bytes = token.encode('utf-8')
        hashed_token_bytes = hashed_token.encode('utf-8')
        return bcrypt.checkpw(token_bytes, hashed_token_bytes)