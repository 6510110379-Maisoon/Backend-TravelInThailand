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

def test_create_province():
    data = {
        "name": "Test Province",
        "is_secondary": False,
        "tax_reduction": 10
    }
    response = client.post("/provinces/", json=data)
    assert response.status_code == 200
    res_json = response.json()
    assert res_json["name"] == data["name"]
    assert res_json["is_secondary"] == data["is_secondary"]
    assert res_json["tax_reduction"] == data["tax_reduction"]
