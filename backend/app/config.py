import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    FRONT_END_URL = os.environ.get("FROT_END_URL", "dummy frontend url");
class DevelopmentConfig(Config):
    DEBUG = True

config_by_name = {
    "development": DevelopmentConfig,
}
