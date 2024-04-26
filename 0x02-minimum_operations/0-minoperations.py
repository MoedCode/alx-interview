#!/usr/bin/python3
"""this is file module contains minOperations function"""


def minOperations(n):
    """minOperations function that calculates the min number of operations"""
    if n <= 1:
        return 0

    result = 0
    i = 2
    while i <= n:
        if n % i == 0:
            result += i
            n /= i
            i -= 1
        i += 1
    return int(result)


# Test cases
if __name__ == "__main__":
    n = 4
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 12

    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
