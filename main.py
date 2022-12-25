from utils import get_stock
from core import me1


prices = get_stock("AMZN")

print(me1(prices))
