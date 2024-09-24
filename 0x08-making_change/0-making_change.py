#!/usr/bin/python3
"""
Module to determine the fewest number
of coins needed to meet a given total.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins
    needed to meet a given amount total.

    Args:
        coins (list of int): A list of the coin values available.
        total (int): The total amount to be met using the fewest coins.

    Returns:
        int: The fewest number of coins needed to meet the total, or -1 if it
             cannot be met with the given coins.
    """
    if total <= 0:
        # If the total is 0 or less, no coins are needed
        return 0

    # Sort the list of coins in descending order to use the largest coins first
    coins.sort(reverse=True)

    # Initialize the count of coins needed
    count = 0
    # Track the remaining amount to be met
    remaining_total = total

    # Iterate through the list of coins
    for coin in coins:
        if remaining_total == 0:
            # If we have already met the total, break out of the loop
            break

        # Determine how many coins of this denomination can be used
        if coin <= remaining_total:
            # Maximum number of this coin to use
            num_coins = remaining_total // coin
            # Add the number of coins to the count
            count += num_coins
            # Reduce the total by the used coins
            remaining_total -= num_coins * coin

    # If the remaining total is 0, return the number of coins used
    # Otherwise, return -1 if the total cannot be met
    return count if remaining_total == 0 else -1
