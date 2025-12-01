from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_order():
    response = client.post("/orders/", json={"shipping_address": "test address"})
    assert response.status_code == 200
    assert "order_id" in response.json()
    assert "status" in response.json()
    assert "total_amount" in response.json()