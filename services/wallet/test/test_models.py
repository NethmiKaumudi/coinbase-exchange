# /wallet/tests/test_models.py

import pytest
from app import create_app, db
from app.model import Wallet

@pytest.fixture
def app():
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_balance(client):
    response = client.get('/balance', query_string={'user_id': 1})
    assert response.status_code == 404
    assert b'Wallet not found' in response.data
