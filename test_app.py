from fastapi.testclient import TestClient
import pytest
from app import app  # import your FastAPI instance

client = TestClient(app)

def test_get_random_name_male():
    response = client.get("/api/random_name/male")
    assert response.status_code == 200
    assert "first_name" in response.json()

def test_get_random_name_female():
    response = client.get("/api/random_name/female")
    assert response.status_code == 200
    assert "first_name" in response.json()

def test_get_random_name_invalid_gender():
    response = client.get("/api/random_name/invalid")
    assert response.status_code == 400
    assert "detail" in response.json()
