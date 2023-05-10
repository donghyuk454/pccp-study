# https://school.programmers.co.kr/tryouts/72091/challenges?language=python3

def solution(prices):
    stack = []
    answer = [0 for _ in range(length)]
    length = len(prices)

    for i in range(length):
        instance = [prices[i], i]
        while stack:
            temp = stack.pop(-1)
            if temp[0] > prices[i]:
                answer[temp[1]] = i - temp[1]
            else:
                stack.append(temp)
                break
        stack.append(instance)

    while stack:
        temp = stack.pop(-1)
        answer[temp[1]] = length - temp[1] - 1

    return answer