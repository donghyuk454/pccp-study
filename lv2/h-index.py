# https://school.programmers.co.kr/tryouts/72073/challenges?language=python3

def solution(citations):
    answer = 0
    citations.sort(reverse=True)

    for i in range(1, len(citations)+1):
        if i > citations[i-1]:
            break
        answer = i

    return answer