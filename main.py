from utils import get_stock
from core import me1, me2


prices = get_stock("AMZN")

print(len(prices))

a = me1(prices)
b = me2(prices)

assert b >= a
