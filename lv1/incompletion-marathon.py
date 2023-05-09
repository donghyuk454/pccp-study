# https://school.programmers.co.kr/tryouts/72081/challenges?language=python3

def solution(participant, completion):
    answer = ''
    result_dict = dict()

    for p in participant:
        result_dict[p] = 0

    for c in completion:
        result_dict[c] += 1

    for key in participant:
        if result_dict[key] == 0:
            answer = key
            break
        result_dict[key] -= 1

    return answer