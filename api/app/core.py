from typing import List, Tuple
import secrets
from pycoin.networks.registry import network_for_netcode
from models.models import (
    Coin,
    AddressCreate,
    AddressInDB,
    PrivateKeyCreate,
    PrivateKeyInDB,
    PrivateKeyReturn,
)
from db.db_config import get_db_connection, Addresses, PrivateKeys
from web3 import Web3, EthereumTesterProvider
from .utils import encrypt_private_key, decrypt_private_key


def _generate_address_and_private_key(coin: Coin) -> Tuple[str, bytes]:
    """
    Generate a cryptocurrency address and its corresponding private key in hexadecimal format,
    based on the specified cryptocurrency coin type.

    Currently, Bitcoin and Ethereum coins are supported. For Bitcoin, the address is generated using the BTC Testnet network
    and for Ethereum, a new account is created using the EthereumTesterProvider from Web3.

    The private key is returned as a hexadecimal string.
    """

    def generate_address_bitcoin():
        coin_network = network_for_netcode("XTN")  # Use the BTC Testnet network
        key = coin_network.keys.private(secret_exponent=secrets.randbits(256))
        address = key.address()
        private_key = key.sec_as_hex()
        return address, private_key

    def generate_address_ethereum():
        w3 = Web3(EthereumTesterProvider())
        account = w3.eth.account.create()
        address = account.address
        private_key = account._private_key.hex()

        return address, private_key

    coin_vs_function = {
        Coin.BTC: generate_address_bitcoin,
        Coin.ETH: generate_address_ethereum,
    }

    return coin_vs_function[coin]()


def get_address(id: int) -> AddressInDB:
    with get_db_connection():
        address = Addresses.get_or_none(id=id)
    return AddressInDB(**(address.__data__)) if address else None


def get_private_key(address: str) -> PrivateKeyReturn:
    with get_db_connection():
        private_key = PrivateKeys.get_or_none(address=address)
    return PrivateKeyReturn(
        address=address,
        encrypted_key=private_key.key,
        decrypted_key=decrypt_private_key(private_key.key),
    )


def list_addresses() -> List[AddressInDB]:
    addresses = Addresses.select().dicts()
    return [address for address in addresses]


def insert_address_into_db(address: AddressCreate) -> AddressCreate:
    _address = Addresses.create(**dict(address))
    return AddressInDB(**(_address.__data__))


def insert_encrypted_private_key_into_db(private_key_obj: PrivateKeyCreate):
    _enc_pvt_key = PrivateKeys.create(**dict(private_key_obj))
    return PrivateKeyInDB(**(_enc_pvt_key.__data__))


def process_address_data_insertion(address: AddressCreate):
    address.address, private_key = _generate_address_and_private_key(address.currency)
    inserted_address = insert_address_into_db(address)

    encrypted_private_key = encrypt_private_key(private_key)
    inserted_private_key = insert_encrypted_private_key_into_db(
        PrivateKeyCreate(
            address=address.address,
            key=encrypted_private_key,
        )
    )

    return {
        "address": inserted_address,
        "private_key": inserted_private_key,
    }
