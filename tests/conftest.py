import pytest

from todo_list_empiretech_back import create_app
from todo_list_empiretech_back.models import db


@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
    })

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()
        db.engine.dispose()


@pytest.fixture
def client(app):
    """Um cliente de teste para simular requisições HTTP."""
    return app.test_client()
