#!/usr/bin/python3
"""solving prime game question """

def isWinner(x, nums):
    """function that checks for the winner"""
    if x < 1 or not nums:
        return None
    max_num = max(nums)

  
# Step 1: Generate primes using Sieve of Eratosthenes
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for i in range(2, int(max_num**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_num + 1, i):
                sieve[j] = False

    # Step 2: Precompute cumulative prime counts
    prime_counts = [0] * (max_num + 1)
    cumulative_count = 0
    for i in range(max_num + 1):
        if sieve[i]:
            cumulative_count += 1
        prime_counts[i] = cumulative_count

    # Step 3: Determine the winner for each game
    maria_wins = 0
    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1

    # Step 4: Compare results
    total_games = len(nums)
    if maria_wins * 2 == total_games:
        return None
    if maria_wins * 2 > total_games:
        return "Maria"
    return "Ben"
