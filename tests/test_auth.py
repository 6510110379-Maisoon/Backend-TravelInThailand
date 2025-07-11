from fastapi.testclient import TestClient
from flasx.main import app

client = TestClient(app)

def test_login():
    client.post("/register/", json={"username": "authuser", "password": "pass"}) # Register a new user for authentication testing
    response = client.post("/auth/token", data={"username": "authuser", "password": "pass"}) # Attempt to login with the registered user's credentials
    assert response.status_code == 200
    assert "access_token" in response.json() # Check that the response contains an access token
