from typing import Tuple, List
import secrets
from pycoin.key import Key
from pycoin.networks.registry import network_for_netcode
from models.models import Coin, AddressCreate, AddressInDB
from db.db_config import get_db_connection, Addresses
from web3 import Web3, EthereumTesterProvider
from eth_account import Account


def _generate_address(coin: Coin):
    def generate_address_bitcoin():
        # XTN represents the BTC Testnet network
        coin_network = network_for_netcode("XTN")
        key = coin_network.keys.private(secret_exponent=secrets.randbits(256))

        return key.address()

    def generate_address_ethereum():
        w3 = Web3(EthereumTesterProvider())
        account = Account.create()
        address = account.address
        private_key = account._private_key.hex()

        return address

    coin_vs_function = {
        Coin.BTC: generate_address_bitcoin,
        Coin.ETH: generate_address_ethereum,
    }

    return coin_vs_function[coin]()


def get_address(id: int):
    with get_db_connection():
        address = Addresses.get_or_none(id=id)
    return AddressInDB(**(address.__data__)) if address else None


def list_addresses() -> List[AddressInDB]:
    addresses = Addresses.select().dicts()
    return [address for address in addresses]


def create_address(address: AddressCreate) -> AddressCreate:
    address.address = _generate_address(address.currency)
    _address = Addresses.create(**dict(address))
    return AddressInDB(**(_address.__data__))
