#!/usr/bin/python3

def sieve_of_eratosthenes(max_n):
    """Generate a list of prime numbers up to max_n using the Sieve of Eratosthenes."""
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while (p * p <= max_n):
        if is_prime[p]:
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1
    return is_prime


def isWinner(x, nums):
    """Determine the winner of the prime game."""
    if not nums or x <= 0:
        return None

    max_n = max(nums)
    is_prime = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = [i for i in range(2, n + 1) if is_prime[i]]
        moves = 0
        while primes:
            prime = primes[0]
            moves += 1
            primes = [p for p in primes if p % prime != 0]

        if moves % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
