from flask.testing import FlaskClient
import pytest
from app import app  # import your Flask instance

client = app.test_client()

def test_get_random_name_male():
    response = client.get("/api/random_name/male")
    assert response.status_code == 200
    assert "first_name" in response.get_json()

def test_get_random_name_female():
    response = client.get("/api/random_name/female")
    assert response.status_code == 200
    assert "first_name" in response.get_json()

def test_get_random_name_invalid_gender():
    response = client.get("/api/random_name/invalid")
    assert response.status_code == 400
    assert "message" in response.get_json()