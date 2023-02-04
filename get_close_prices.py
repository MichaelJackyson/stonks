import sys

import numpy as np

from utils import get_stock


def main(symbol: str) -> None:

    prices = get_stock(symbol, period="max")
    
    if len(prices) > 0:
        np.save("{}".format(symbol), prices)
        print("NYSE [{}] prices saved with {} records".format(symbol, len(prices)))
    else:
        print("Stock not found!")

if __name__ == "__main__":
    assert len(sys.argv) == 2, "Usage: python3 get_close_prices.py [symbol]"
    main(sys.argv[1])
