from datetime import datetime
from typing import Optional
from enum import Enum
from pydantic import BaseModel


class Coin(str, Enum):
    BTC = "btc"
    ETH = "eth"


class AddressCreate(BaseModel):
    address: Optional[str]
    label: Optional[str]
    balance: Optional[float]
    currency: Coin
    creation_date: Optional[datetime]
    last_used: Optional[datetime]
    description: Optional[str]
    status: Optional[str]


class AddressInDB(AddressCreate):
    id: int
