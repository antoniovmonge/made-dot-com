import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers

from src import app, db
from src.orm import metadata, start_mappers

# FIXTURES FROM TDD FLASK DOCKER
@pytest.fixture(scope="module")
def test_app():
    app.config.from_object("src.config.TestingConfig")
    with app.app_context():
        yield app


@pytest.fixture(scope="module")
def test_database():
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()

# FIXTURES FROM PYTHON ARCHITECTURE PATTERNS
@pytest.fixture
def in_memory_db():
    engine = create_engine("sqlite:///:memory:")
    metadata.create_all(engine)
    return engine


@pytest.fixture
def session(in_memory_db):
    start_mappers()
    yield sessionmaker(bind=in_memory_db)()
    clear_mappers()
