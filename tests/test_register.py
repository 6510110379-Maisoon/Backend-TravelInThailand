from fastapi.testclient import TestClient
from flasx.main import app

client = TestClient(app)

def test_register():
    response = client.post("/register/", json={"username": "testuser", "password": "pass"})
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"