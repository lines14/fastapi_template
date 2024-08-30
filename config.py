import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
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
    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    )


settings = Settings()
def get_DB_URL():
    return (f"mysql+aiomysql://root:{settings.DB_ROOT_PASSWORD}@"
            f"{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}")