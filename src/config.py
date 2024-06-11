import os

class BaseConfig:
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "my_precious"


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_TEST_URL")


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


def get_postgres_uri():
    # host = os.environ.get("DB_HOST", "localhost")
    # port = 54321 if host == "localhost" else 5432
    # password = os.environ.get("DB_PASSWORD", "abc123")
    # user, db_name = "allocation", "allocation"
    # return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
    return os.environ.get("DATABASE_TEST_URL")


def get_api_url():
    host = os.environ.get("API_HOST", "localhost")
    port = 5000 if host == "localhost" else 80
    return f"http://{host}:{port}"
