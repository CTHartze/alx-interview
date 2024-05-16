#!/usr/bin/python3
"""Prime Game problem"""


def isWinner(x, nums):
    def sieve_of_eratosthenes(n):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1
        return [i for i in range(n + 1) if primes[i]]

    def play_game(n):
        primes = sieve_of_eratosthenes(n)
        maria_turn = True
        while True:
            if not primes:
                return "Ben" if maria_turn else "Maria"
            next_prime = primes[0]
            if maria_turn:
                maria_turn = False
            else:
                primes = [num for num in primes if num % next_prime != 0]
                maria_turn = True

    # Play each round and keep track of the winner
    maria_wins = ben_wins = 0
    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
