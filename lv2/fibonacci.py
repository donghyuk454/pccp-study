# https://school.programmers.co.kr/tryouts/72086/challenges?language=python3

import sys
sys.setrecursionlimit(10 ** 6)

def solution(n):
    answer = 0

    dp = [-1 for _ in range(n+1)]
    dp[0] = 0
    dp[1] = 1

    def fibonacci(n):
        if dp[n] != -1:
            return dp[n]

        dp[n] = fibonacci(n-1) + fibonacci(n-2)
        return dp[n]

    return fibonacci(n) % 1234567

