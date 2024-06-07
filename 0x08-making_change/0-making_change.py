#!/usr/bin/env python3
"""coin change problem"""


def makeChange(coins, total):
    """determine the fewest number of coins to meet a given amount total"""
    if total <= 0:
        return 0
    coins = sorted(coins, reverse=True)
    change = 0
    for coin in coins:
        if total <= 0:
            break
        change += total // coin
        total = total % coin
    if total != 0:
        return -1
    return change
