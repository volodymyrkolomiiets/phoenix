import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    user = os.environ.get('MYSQL_USER')
    user_password = os.environ.get("MYSQL_PASSWORD")
    mysql_host = os.environ.get("MYSQL_HOST")
    mysql_port = os.environ.get("MYSQL_PORT")
    mysql_db = os.environ.get("MYSQL_DB")

    ENV = 'development'
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{user}:{user_password}@product_dev_db:{mysql_port}/{mysql_db}'
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    pass
