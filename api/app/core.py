from typing import Tuple, List
import secrets
from pycoin.key import Key
from pycoin.networks.registry import network_for_netcode
from models.models import Coin
from db.db_config import get_db_connection, get_table_column_names

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
        columns = get_table_column_names(table_name="addresses")
        row = c.execute("SELECT * FROM addresses WHERE id=?", (c.lastrowid,)).fetchone()

    return dict(zip(columns, row))


def generate_address(coin: Coin):
    coin_network = coin_vs_network[coin]
    key = coin_network.keys.private(secret_exponent=secrets.randbits(256))

    return _insert_address(key.address(), coin.value)


def list_addresses():
    with get_db_connection() as conn:
        table_name = "addresses"
        c = conn.cursor()
        rows = c.execute(f"SELECT * FROM {table_name}").fetchall()
        columns = get_table_column_names(table_name)

    return [dict(zip(columns, row)) for row in rows]
