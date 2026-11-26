from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Enterprise Data Operations Platform"
    DATABASE_URL: str = "sqlite:///./enterprise_data.db"
    DEBUG: bool = True

    class Config:
        env_file = ".env"


settings = Settings()