#!/usr/bin/env python3
from sys import argv


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def pick_a_prime(num_list):
    for i in num_list:
        if is_prime(i):
            num_list.remove(i)
            num_list[:] = [num for num in num_list if num %
                           i != 0]  # Remove multiples of the prime
            return i
    return False


def simulate_round(n):
    Maria = True
    Ben = True
    turn = 0  # 0 for Maria, 1 for Ben
    pick_list = list(range(1, n + 1))

    while True:
        if turn == 0:
            if not pick_a_prime(pick_list):
                return "Ben"  # Maria cannot make a move
        else:
            if not pick_a_prime(pick_list):
                return "Maria"  # Ben cannot make a move
        turn = 1 - turn  # Switch turns


def isWinner(x, nums):
    if not nums or x <= 0:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = simulate_round(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    # Example usage
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

    # Uncomment for command line argument testing
    # if len(argv) > 1:
    #     print(is_prime(int(argv[1])))
