# https://school.programmers.co.kr/tryouts/72083/challenges?language=python3

def solution(clothes):
    answer = 1
    clothes_dict = dict()

    for cloth in clothes:
        if cloth[1] not in clothes_dict:
            clothes_dict[cloth[1]] = []
        clothes_dict[cloth[1]].append(cloth[0])

    for key in clothes_dict:
        answer *= len(clothes_dict[key])+1
    answer -= 1

    return answer