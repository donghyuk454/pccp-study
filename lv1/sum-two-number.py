# https://school.programmers.co.kr/tryouts/72072/challenges?language=python3

def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue
            value = numbers[i] + numbers[j]
            if value not in answer:
                answer.append(value)
    answer.sort()

    return answer