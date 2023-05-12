import os
import uvicorn
from fastapi import FastAPI
from models.models import Coin
from db.db_config import init_db

app = FastAPI()
PORT = os.environ["PORT"]


@app.get("/")
def home():
    return {"message": "zeply test"}


@app.post("/addresses/generate")
async def generate_address(coin: Coin):
    pass


@app.get("/addresses/{address_id}")
def get_address(address_id: int):
    pass


@app.get("/addresses")
def get_addresses():
    pass


@app.on_event("startup")
async def startup_event():
    init_db()


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8020, reload=True)
