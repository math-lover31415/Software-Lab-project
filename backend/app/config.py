import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")


class Config:
    FRONT_END_URL = os.environ.get("FRONT_END_URL", "dummy frontend url")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "postgresql://fireheatmap:fireheatmap@localhost:5432/firemap"
    )
    
class DevelopmentConfig(Config):
    DEBUG = True

config_by_name = {
    "development": DevelopmentConfig,
}
