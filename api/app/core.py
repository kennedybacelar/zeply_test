from typing import Tuple
import secrets
from pycoin.key import Key
from pycoin.networks.registry import network_for_netcode
from models.models import Coin
from db.db_config import get_db_connection

coin_vs_network = {
    Coin.BTC: network_for_netcode("XTN"),  # XTN represents the BTC Testnet network
}


def _insert_address(address: str, currency: str) -> Tuple:
    with get_db_connection() as conn:
        c = conn.cursor()
        c.execute(
            "INSERT INTO addresses (address, currency) VALUES (?, ?)",
            (address, currency),
        )

        return c.execute(
            "SELECT * FROM addresses WHERE id=?", (c.lastrowid,)
        ).fetchone()


def generate_address(coin: Coin):
    coin_network = coin_vs_network[coin]
    key = coin_network.keys.private(secret_exponent=secrets.randbits(256))

    return _insert_address(key.address(), coin.value)
