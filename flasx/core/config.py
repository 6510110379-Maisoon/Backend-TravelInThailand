from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "supersecret"
    SQLDB_URL: str = "sqlite:///./travel_thai_half.db" # Database URL connection string (SQLite)

    class Config:
        env_file = ".env"

settings = Settings()
