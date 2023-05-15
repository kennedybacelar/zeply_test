import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.core import process_address_data_insertion, get_address, list_addresses


client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "zeply test"}


def test_generate_address():
    address_data = {
        "name": "Test Address",
        "currency": "BTC",
        "description": "Test Description",
    }
    response = client.post("/addresses/generate", json=address_data)
    assert response.status_code == 200
    assert response.json().get("address")
    assert response.json().get("private_key")


def test_get_address():
    address_data = {
        "name": "Test Address",
        "currency": "BTC",
        "description": "Test Description",
    }
    address = process_address_data_insertion(address_data)["address"]
    response = client.get(f"/addresses/{address.id}")
    assert response.status_code == 200
    assert response.json() == address.dict()


def test_list_addresses():
    address_data = {
        "name": "Test Address",
        "currency": "BTC",
        "description": "Test Description",
    }
    addresses = [
        process_address_data_insertion(address_data)["address"] for _ in range(3)
    ]
    response = client.get("/addresses")
    assert response.status_code == 200
    assert response.json() == [address.dict() for address in addresses]
