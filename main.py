from utils import get_stock
from core import me1, me2


prices = get_stock("AMZN")


a = me1(prices)
b = me2(prices)
