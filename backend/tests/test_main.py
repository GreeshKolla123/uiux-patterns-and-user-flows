from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_user():
    response = client.post('/auth/register', json={'username': 'testuser', 'email': 'test@example.com', 'password': 'password'})
    assert response.status_code == 200

def test_login_user():
    response = client.post('/auth/login', data={'grant_type': 'password', 'username': 'testuser', 'password': 'password'})
    assert response.status_code == 200

def test_read_products():
    response = client.get('/products')
    assert response.status_code == 200

def test_read_product():
    response = client.get('/products/1')
    assert response.status_code == 200

def test_add_to_cart():
    response = client.post('/cart/add', json={'product_id': 1, 'quantity': 2})
    assert response.status_code == 200

def test_read_cart():
    response = client.get('/cart')
    assert response.status_code == 200

def test_create_order():
    response = client.post('/orders', json={'shipping_address': '123 Main St'})
    assert response.status_code == 200