import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    CURRENCY_RATES_URL: str
    REDIS_HOST: str
    REDIS_PASSWORD: str
    REDIS_PORT: int
    DB_NAME: str
    DB_ROOT_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    TTL: int
    ALGORITHM: str
    model_config = SettingsConfigDict(env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))

    @property
    def DB_URL(self) -> str:
        return (f"mysql+aiomysql://root:{self.DB_ROOT_PASSWORD}@"
                f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}")