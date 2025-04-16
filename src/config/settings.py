import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Motorcycle API"
    
    # Database
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", "mysql+pymysql://username:password@localhost:3306/motorcycle_api"
    )
    
    # JWT
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-here")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Tax settings
    TAX_RATE: float = 0.16  # 16%
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()