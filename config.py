# config.py
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Config:
    SECRET_KEY = 'O0tvhi2D67NPhHiJK6VLPw'
    SQLALCHEMY_TRACK_MODIFICATION = False


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://'
    SQLALCHEMY_ECHO=True

class ProductionConfig(Config):
    pass