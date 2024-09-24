#!/usr/bin/python3
"""Module for makeChange function"""


def makeChange(coins, total):
    """
    Function to determine the fewest number of coins to make up total

    Args:
        coins: list of the values of the coins in your possession
    total: total amount to be made up

    Returns:
        0 if total is 0 or less
    -1 if total cannot be made up by any
    fewest number of coins to meet total otherwise
    """
    if total <= 0:
        return 0

    if not coins:
        return -1

    coins.sort(reverse=True)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
