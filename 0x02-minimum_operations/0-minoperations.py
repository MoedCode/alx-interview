#!/usr/bin/python3
"""this is file module contains minOperations function"""


def minOperations(n):
    """
    minOperations function that calculates the min
    number of operations needed to reach n numbere
    of chars
    Args:
        n: number of characters, int
    Return:
        result: number of operations needed, int
    """

    if n <= 0:
        return 0

    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n] if dp[n] != float('inf') else 0


# Test cases
if __name__ == "__main__":
    n = 4
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 12

    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
