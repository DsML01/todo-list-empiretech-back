from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )

    #Deixando todos os campos como opcionais para fins didáticos
    DATABASE_URL: str = Field(default="sqlite:///todo_list.db", description="Database connection URL")
    FLASK_PORT: int = Field(default=5000)
    FLASK_DEBUG: bool = Field(default=False)

settings = Settings()