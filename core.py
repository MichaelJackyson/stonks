from typing import List


def me1(prices: List[float]) -> float:

    start_index = 0
    dee_snuts = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[start_index]:
            if prices[i] - prices[start_index] > dee_snuts:
                dee_snuts = prices[i] - prices[start_index]
        else:
            start_index = i
    
    return dee_snuts



