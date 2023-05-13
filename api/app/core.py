from typing import Tuple, List
import secrets
from pycoin.key import Key
from pycoin.networks.registry import network_for_netcode
from models.models import Coin, AddressCreate, AddressInDB
from db.db_config import get_db_connection, Addresses

coin_vs_network = {
    Coin.BTC: network_for_netcode("XTN"),  # XTN represents the BTC Testnet network
}


def _generate_address(coin: Coin):
    coin_network = coin_vs_network[coin]
    key = coin_network.keys.private(secret_exponent=secrets.randbits(256))

    return key.address()


def get_address(id: int):
    with get_db_connection():
        address = Addresses.get_or_none(id=id)
    return AddressInDB(**(address.__data__)) if address else None


def list_addresses() -> List[dict]:
    addresses = Addresses.select().dicts()
    return [address for address in addresses]


def create_address(address: AddressCreate) -> AddressCreate:
    address.address = _generate_address(address.currency)
    _address = Addresses.create(**dict(address))
    return _address.__data__
