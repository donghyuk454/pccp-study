# https://school.programmers.co.kr/tryouts/72114/challenges?language=python3

def solution(numbers, target):
    answer = 0
    candidates = [0]

    for number in numbers:
        temp = []
        for candidate in candidates:
            temp.append(candidate + number)
            temp.append(candidate - number)
        candidates = temp

    for candidate in candidates:
        if candidate == target:
            answer += 1

    return answer