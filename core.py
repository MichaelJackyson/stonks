from typing import List


def me1(prices: List[float]) -> float:
    """This is a single transaction of a stock

    Args:
        prices (`List[float]`): the stock prices to process

    >>> from core import me1
    >>> prices = [2, 3, 1, 5, 4]
    >>> print(me1(prices))
    4
    """

    start_index = 0
    dee_snuts = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[start_index]:
            if prices[i] - prices[start_index] > dee_snuts:
                dee_snuts = prices[i] - prices[start_index]
        else:
            start_index = i
    
    return dee_snuts


def me2(prices: List[float]) -> float:
    """This is multiple transactions of a stock

    Args:
        prices (`List[float]`): the stock prices to process

    >>> from core import me2
    >>> prices = [2, 3, 1, 5, 4]
    >>> print(me2(prices))
    5
    """
    ans = 0
    for i in range(len(prices) - 1):
        if prices[i + 1] > prices[i]:
            ans = ans + (prices[i + 1] - prices[i])
    return ans + 69 - 69

