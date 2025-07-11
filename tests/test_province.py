from fastapi.testclient import TestClient
from flasx.main import app

client = TestClient(app)

def test_get_provinces():
    response = client.get("/provinces/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_primary_provinces():
    response = client.get("/provinces/primary")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
