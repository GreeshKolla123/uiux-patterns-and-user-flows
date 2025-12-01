from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = 'postgresql://user:password@localhost/dbname'
    SECRET_KEY: str = 'dev-secret-key-change-in-production'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    class Config:
        env_file = '.env'