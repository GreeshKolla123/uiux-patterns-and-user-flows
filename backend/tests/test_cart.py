from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_to_cart():
    response = client.post('/api/cart', json={'product_id': 1, 'quantity': 2})
    assert response.status_code == 200

def test_get_cart():
    response = client.get('/api/cart')
    assert response.status_code == 200