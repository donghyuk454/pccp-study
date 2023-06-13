# https://school.programmers.co.kr/tryouts/72117/challenges?language=python3

def solution(p):
    answer = do(p)
    return answer

def do(w):
    if w == "":
        return ""
    count = 0
    if w[0] == "(":
        count += 1
    else:
        count -= 1

    idx = 1
    while idx < len(w) and count != 0:
        if w[idx] == "(":
            count += 1
        else:
            count -= 1
        idx += 1
    u = w[:idx]
    v = w[idx:]
    if u[0] == "(":
        return u + do(v)

    result = "(" + do(v) + ")"

    temp = u[1:-1]
    for t in temp:
        if t == "(":
            result += ")"
        else:
            result += "("
    return result