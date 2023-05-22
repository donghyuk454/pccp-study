# https://school.programmers.co.kr/tryouts/72087/challenges?language=python3

def solution(N, number):
    answer = 2
    if number == N:
        return 1

    cases = dict()
    cases[0] = set([0])
    cases[1] = set([N])

    while answer <= 8:
        avail_case = set()
        for step in range(1, answer):
            value = get_step_value(N, step)

            avail_case.add(get_step_value(N,answer))
            for case in cases[answer-step]:
                avail_case.add(case+value)
                avail_case.add(case-value)
                avail_case.add(case*value)
                if value != 0 and case % value == 0:
                    avail_case.add(case//value)
                if case != 0 and value % case == 0:
                    avail_case.add(value//case)
                avail_case.add(value-case)

        if number in avail_case:
            return answer
        cases[answer] = avail_case
        answer += 1

    return answer if answer < 9 else -1

def get_step_value(N, step):
    temp = ""
    for _ in range(step):
        temp += str(N)
    return int(temp)