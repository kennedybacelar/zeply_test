import os
import uvicorn
from fastapi import FastAPI
from models.models import Coin

app = FastAPI()
PORT = os.environ["PORT"]


@app.post("/addresses/generate")
async def generate_address(coin: Coin):
    pass


@app.get("/addresses/{address_id}")
def get_address(address_id: int):
    pass


@app.get("/addresses")
def get_addresses():
    pass


if __name__ == "__main__":
    uvicorn.run("api.main:app", host="0.0.0.0", port=8020, reload=True)
