#!/usr/bin/python3
"""
Coin change problem
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    # Initialize list to store coin values
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0  # Base case: 0 coins needed to make change for 0 total

    for coin in coins:
        for amount in range(coin, total + 1):
            # Update minimum number of coins needed for each total
            min_coins[amount] = min(min_coins[amount], min_coins[amount - coin] + 1)

    return min_coins[total] if min_coins[total] != float('inf') else -1
