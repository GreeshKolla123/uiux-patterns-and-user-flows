from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post('/api/register', json={'username': 'john_doe', 'email': 'john@example.com', 'password': 'password123'})
    assert response.status_code == 200