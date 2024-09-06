# /api-gateway/tests/test_routes.py

import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config.from_object('app.config.TestConfig')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_trade(client):
    response = client.post('/trade', json={'action': 'buy', 'quantity': 10})
    assert response.status_code == 200
    assert b'Trade request forwarded' in response.data

def test_balance(client):
    response = client.get('/balance')
    assert response.status_code == 200
    assert b'Balance request forwarded' in response.data

def test_login(client):
    response = client.post('/login', json={'username': 'user', 'password': 'pass'})
    assert response.status_code == 200
    assert b'Login request forwarded' in response.data

def test_logout(client):
    response = client.post('/logout', json={'username': 'user'})
    assert response.status_code == 200
    assert b'Logout request forwarded' in response.data
