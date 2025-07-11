from fastapi.testclient import TestClient
from flasx.main import app

client = TestClient(app)

def test_add_target():
    client.post("/register/", json={"username": "targetuser", "password": "pass"})
    login_res = client.post("/auth/token", data={"username": "targetuser", "password": "pass"})
    token = login_res.json()["access_token"]
    client.post("/provinces/", json={"name": "Chiang Mai", "is_secondary": True, "tax_reduction": 15})
    response = client.post("/targets/", json={"province_id": 1}, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200