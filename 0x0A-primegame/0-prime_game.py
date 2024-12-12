#!/usr/bin/python3
"""solving prime game question """

def isWinner(x, nums):
    if x < 1 or not nums:
        return None
    max_num = max(nums)

  
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False  

    for i in range(2, int(max_num**0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, max_num + 1, i):
                is_prime[multiple] = False
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
