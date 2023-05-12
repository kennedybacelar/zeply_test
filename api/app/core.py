from pycoin.key import Key
from pycoin.networks.registry import network_for_netcode
from models.models import Coin

coin_vs_network = {
    Coin.BTC: network_for_netcode("XTN"),  # XTN represents the BTC Testnet network
}


def generate_address(coin: Coin):
    coin_network = coin_vs_network[coin]
    key = coin_network.keys.private(secret_exponent=1)

    return key.address()
