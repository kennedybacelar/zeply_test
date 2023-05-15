import os
import uvicorn
from typing import Dict, List, Union
from fastapi import FastAPI, HTTPException
from models.models import AddressCreate, AddressInDB, PrivateKeyInDB
from db.db_config import init_db, DB_STR_CONNECTION

from .core import process_address_data_insertion, list_addresses, get_address
from .utils import dev_fernet_key_setup, FERNET_KEY_FILE_PATH

__author__ = "Kennedy Bacelar"

app = FastAPI(title="Zeply REST API")
PORT = os.environ.get("PORT") or 8020


@app.get("/")
def home_():
    return {"message": "Welcome to the Zeply API"}


@app.post(
    "/addresses/generate", response_model=Dict[str, Union[AddressInDB, PrivateKeyInDB]]
)
async def create_address(
    address: AddressCreate,
) -> Dict[str, Union[AddressInDB, PrivateKeyInDB]]:
    address = process_address_data_insertion(address)
    if not address:
        raise HTTPException(status_code=400, detail="Address creation failed")
    return address


@app.get("/addresses/{address_id}", response_model=AddressInDB)
def read_address(address_id: int) -> AddressInDB:
    address = get_address(address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    return address


@app.get("/addresses", response_model=List[AddressInDB])
def read_addresses() -> List[AddressInDB]:
    return list_addresses()


@app.on_event("startup")
async def startup_event():
    _remove_config_files()
    init_db()
    dev_fernet_key_setup()


@app.on_event("shutdown")
async def shutdown_event():
    _remove_config_files()


def _remove_config_files():
    if os.path.exists(DB_STR_CONNECTION):
        os.remove(DB_STR_CONNECTION)

    if os.path.exists(FERNET_KEY_FILE_PATH):
        os.remove(FERNET_KEY_FILE_PATH)


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8020, reload=True)
