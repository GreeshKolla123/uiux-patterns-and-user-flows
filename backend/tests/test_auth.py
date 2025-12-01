from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_user():
    response = client.post("/auth/register", data={"username": "testuser", "password": "testpassword"})
    assert response.status_code == 200
    assert "user_id" in response.json()
    assert "username" in response.json()
    assert "email" in response.json()
    assert "role" in response.json()