# /trading/tests/test_models.py

import pytest
from app import create_app, db
from app.models import Trade

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

def test_trade(client):
    response = client.post('/trade', json={'user_id': 1, 'asset': 'AAPL', 'quantity': 10, 'price': 150})
    assert response.status_code == 200
    assert b'Trade completed' in response.data
