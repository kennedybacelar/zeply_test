import os
import uvicorn
from fastapi import FastAPI
from models.models import AddressCreate
from db.db_config import init_db, DB_STR_CONNECTION

from .core import process_address_data_insertion, list_addresses, get_address
from .utils import dev_fernet_key_setup, FERNET_KEY_FILE_PATH

__author__ = "Kennedy Bacelar"

app = FastAPI(title="Zeply REST API")
PORT = os.environ.get("PORT") or 8020


@app.get("/")
def home_():
    return {"message": "zeply test"}


@app.post("/addresses/generate")
async def generate_address_(address: AddressCreate):
    return process_address_data_insertion(address)


@app.get("/addresses/{address_id}")
def get_address_(address_id: int):
    return get_address(address_id)


@app.get("/addresses")
def list_addresses_():
    return list_addresses()


@app.on_event("startup")
async def startup_event():
    init_db()
    dev_fernet_key_setup()


@app.on_event("shutdown")
async def shutdown_event():
    os.remove(DB_STR_CONNECTION)
    os.remove(FERNET_KEY_FILE_PATH)


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8020, reload=True)
