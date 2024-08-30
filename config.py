import os
import classutilities
from typing import ClassVar
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
    DB_URL = ClassVar[str]
    model_config = SettingsConfigDict(env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.DB_URL = (f"mysql+aiomysql://root:{self.DB_ROOT_PASSWORD}@"
                       f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}")
        
    @classutilities.classproperty
    def DB_URL(self):
        return self.DB_URL