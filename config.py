import os
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseModel):
    app_name: str = "Fast Todo App"
    access_token_expire_minutes: str = os.environ.get(
        "ACCESS_TOKEN_EXPIRE_MINUTES", "5"
    )
    refresh_token_expire_minutes: str = os.environ.get(
        "REFRESH_TOKEN_EXPIRE_MINUTES", "10"
    )
    secret_key: str = os.environ.get("SECRET_KEY", "VT3BlbkFJmqaji32ruwrd43jmhb3s")
    algorithm: str = os.environ.get("ALGORITHM", "HS256")

    @property
    def database_url(self):
        return f"postgresql://{os.environ['DATABASE_USERNAME']}:{os.environ['DATABASE_PASSWORD']}@{os.environ['DATABASE_HOST']}/{os.environ['DATABASE_NAME']}?sslmode=require"

    class ConfigDict:
        env_file = ".env"


settings = Settings()
