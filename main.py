from utils import get_stock, get_date_list, get_stock_price_date, draw_graph
from core import me1, me2


# prices = get_stock("TSLA")
price_date = get_stock_price_date(target="ETH-USD", period="3y")
prices = list(price_date.values())


def average(prices):
    return sum(prices) / len(prices)


print(average(prices))
exit()


draw_graph(list(price_date.keys()), list(price_date.values()))

# print(len(prices))

# a = me1(prices)
# b = me2(prices)

# assert b >= a
