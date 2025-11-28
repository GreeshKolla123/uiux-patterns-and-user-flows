from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_complete_checkout():
    response = client.post('/api/checkout', json={'payment_method': 'credit_card', 'shipping_address': {'name': 'John Doe', 'address': '123 Main St', 'city': 'Anytown', 'state': 'CA', 'zip': '12345'}})
    assert response.status_code == 200