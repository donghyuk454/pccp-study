# https://school.programmers.co.kr/tryouts/72064/challenges?language=python3

def solution(word):
    answer = 0
    all_case = []

    def set_case(now):
        if len(now) > 5:
            return

        all_case.append(now)
        if len(now) == 5:
            return

        alpha = ["A", "E", "I", "O", "U"]
        for a in alpha:
            value = set_case(now+a)

    alpha = ["A", "E", "I", "O", "U"]
    for a in alpha:
        set_case(a)

    for i in range(len(all_case)):
        if all_case[i] == word:
            return i+1

    return answer