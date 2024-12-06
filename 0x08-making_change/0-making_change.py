#!/usr/bin/python3
"""
0-making_change.py: A script to determine the minimum number of coins
needed to make change for a given amount.
"""


def makeChange(coins, total):
    """
    Determines the minimum number of coins needed to make change for `total`.

    Args:
        coins (list): A list of coin denominations.
        total (int): The total amount of change required.

    Returns:
        int: The minimum number of coins needed to make the change.
             Returns -1 if the change cannot be made.
    """
    if total <= 0:
        return 0  # No coins needed if total is 0 or negative

    coins.sort(reverse=True)  # Sort coins in descending order
    coin_count = 0
    index = 0

    while total > 0:
        if index >= len(coins):  # No coins left to try
            return -1

        if total >= coins[index]:  # Use the current coin if it fits
            total -= coins[index]
            coin_count += 1
        else:
            index += 1  # Move to the next smaller coin

    return coin_count
