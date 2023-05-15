from datetime import datetime
from typing import Optional
from enum import Enum
from pydantic import BaseModel, validator


class Coin(str, Enum):
    BTC = "btc"
    ETH = "eth"


class AddressCreate(BaseModel):
    address: Optional[str]
    label: Optional[str]
    balance: Optional[float] = 0
    currency: Coin
    creation_date: Optional[datetime] = datetime.utcnow().isoformat()
    last_used: Optional[datetime]
    description: Optional[str]
    status: Optional[str]


class AddressInDB(AddressCreate):
    id: int


class PrivateKeyCreate(BaseModel):
    address: str
    key: str


class PrivateKeyInDB(PrivateKeyCreate):
    id: int


class AddressTestAssertFormat(BaseModel):
    address: str
    currency: str
