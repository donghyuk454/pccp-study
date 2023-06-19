# https://school.programmers.co.kr/tryouts/72074/challenges?language=python3

def solution(strings, n):
    answer = strings[:]
    answer.sort()
    answer.sort(key=lambda x:x[n])
    return answer