from fastapi.testclient import TestClient

from app.main import app
from app.core import process_address_data_insertion, get_address, list_addresses
from models.models import AddressCreate, AddressTestAssertFormat


client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Zeply API"}


def test_generate_address():
    address_data = {
        "name": "Test Address",
        "currency": "btc",
        "description": "Test Description",
    }
    response = client.post("/addresses/generate", json=address_data)
    assert response.status_code == 200
    assert response.json().get("address")
    assert response.json().get("private_key")


def test_get_address():
    address_data = {
        "name": "Test Address",
        "currency": "btc",
        "description": "Test Description",
    }
    address_data_parsed = AddressCreate(**address_data)
    address = process_address_data_insertion(address_data_parsed)["address"]
    response = client.get(f"/addresses/{address.id}")
    assert response.status_code == 200
    assert response.json()["id"] == address.dict()["id"]
    assert response.json()["address"] == address.dict()["address"]


def test_list_addresses():
    num_iterations = 1
    address_data = {
        "name": "Test Address",
        "currency": "btc",
        "description": "Test Description",
    }

    # Create expected addresses
    created_addresses = [
        process_address_data_insertion(AddressCreate(**address_data))["address"]
        for _ in range(num_iterations)
    ]

    expected_addresses = [
        AddressTestAssertFormat(**dict(created_address))
        for created_address in created_addresses
    ]

    # Get actual addresses from the server response
    response = client.get("/addresses")
    response_json = response.json()
    returned_addresses = [
        AddressTestAssertFormat(**ret_address)
        for ret_address in response_json[-num_iterations:]
    ]

    # Compare expected and actual addresses
    assert response.status_code == 200
    assert returned_addresses == expected_addresses
