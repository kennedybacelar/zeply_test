import os
import uvicorn
from fastapi import FastAPI
from models.models import Coin
from db.db_config import init_db, DB_STR_CONNECTION
from .core import generate_address

app = FastAPI(title="Zeply REST API")
PORT = os.environ.get("PORT") or 8020


@app.get("/")
def home_():
    return {"message": "zeply test"}


@app.post("/addresses/generate/{coin}")
async def generate_address_(coin: Coin):
    return generate_address(coin)


@app.get("/addresses/{address_id}")
def get_address_(address_id: int):
    pass


@app.get("/addresses")
def get_addresses_():
    pass


@app.on_event("startup")
async def startup_event():
    init_db()


@app.on_event("shutdown")
async def shutdown_event():
    os.remove(DB_STR_CONNECTION)


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8020, reload=True)
