# https://school.programmers.co.kr/tryouts/72057/challenges?language=python3

def solution(n):
    answer = 0

    value = ''
    while n > 0:
        n, mod = divmod(n, 3)
        value += str(mod)

    value = value[::-1]
    for i in range(len(value)):
        answer += int(value[i])*(3**i)

    return answer