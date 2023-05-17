# https://school.programmers.co.kr/tryouts/72113/challenges?language=python3

def solution(n, k):
    answer = []
    numbers = [i for i in range(1, n+1)]
    value = n-1

    while value >= 0 and k > 1:
        temp = factorial(value)
        div = k // temp
        k = k % temp
        if k == 0:
            answer.append(numbers.pop(div-1))
            break
        answer.append(numbers.pop(div))
        value -= 1

    if k == 0:
        numbers.sort(reverse=True)
    for n in numbers:
        answer.append(n)

    return answer

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result