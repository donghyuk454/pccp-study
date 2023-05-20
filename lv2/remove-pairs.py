# https://school.programmers.co.kr/tryouts/72055/challenges?language=python3

def solution(s):
    stack = []

    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i])
            continue

        if stack[-1] == s[i]:
            stack.pop(-1)
        else:
            stack.append(s[i])

    return 1 if len(stack) == 0 else 0