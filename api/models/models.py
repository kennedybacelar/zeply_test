from enum import Enum
from pydantic import BaseModel


class Coin(str, Enum):
    BTC = "btc"
    ETH = "eth"


class AddressInDB(BaseModel):
    id: int
    address: str
    currency: str
