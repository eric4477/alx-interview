#!/usr/bin/python3
"""Module defining isWinner function."""


def isWinner(x, nums):
    if x <= 0 or not nums:
        return None

    # Find the maximum n we need to check to build sieve
    max_n = max(nums)

    # Sieve of Eratosthenes to determine primes up to max_n
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
    for start in range(2, int(max_n**0.5) + 1):
        if sieve[start]:
            for multiple in range(start * start, max_n + 1, start):
                sieve[multiple] = False

    # List of primes up to max_n
    primes = [i for i in range(max_n + 1) if sieve[i]]

    # Calculate the winner for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_up_to_n = [p for p in primes if p <= n]
        prime_count = len(primes_up_to_n)

        # Maria wins if the number of primes up to n is odd, Ben wins if even
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
