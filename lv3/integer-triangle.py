# https://school.programmers.co.kr/tryouts/72088/challenges?language=python3

def solution(triangle):
    dp = []

    for tri in triangle:
        value = [-1 for _ in range(len(triangle))]
        dp.append(value)

    def find(x, y):
        if x == len(triangle)-1:
            return triangle[x][y]

        if dp[x][y] != -1:
            return dp[x][y]

        value1 = find(x+1, y)
        value2 = find(x+1, y+1)
        dp[x][y] = max(value1, value2) + triangle[x][y]

        return dp[x][y]

    return find(0,0)