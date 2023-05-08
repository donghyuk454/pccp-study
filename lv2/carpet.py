# https://school.programmers.co.kr/tryouts/72068/challenges?language=python3

def solution(brown, yellow):
    answer = []
    carpet = brown + yellow

    for height in range(1, carpet+1):
        if carpet % height != 0:
            continue
        width = carpet // height
        if brown == 2*(width+height-2):
            answer = [width, height]
            break

    return answer