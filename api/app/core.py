from pycoin.key import Key
from pycoin.networks import BitcoinMainnet, EthereumMainnet
from models.models import Coin

coin_vs_network = {
    Coin.BTC: BitcoinMainnet,
    Coin.ETH: EthereumMainnet,
}


def generate_address(coin: Coin):
    coin_network = coin_vs_network[coin]
    key = Key.generate(network=coin_network)
    return key.address()
