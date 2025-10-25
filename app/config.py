from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MONGODB_URL: str
    MONGO_DB_NAME: str

    REDIS_HOST: str = "localhost"
    REDIST_PORT: int = 6379
    REDIS_DB: int = 0
    REDIS_CACHE_EXPIRE: int = 300

    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    DEBUG: bool = False
    LEVEL: str = "INFO"
    APP_NAME: str = "ecommerce-fastapi"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
