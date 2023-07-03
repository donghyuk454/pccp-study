# https://school.programmers.co.kr/tryouts/72121/challenges

from copy import deepcopy

def solution(name):
    answer = 0
    visited = [False for _ in range(len(name))]
    for i in range(len(name)):
        if name[i] == 'A':
            visited[i] = True

    for n in name:
        answer += min(ord(n)-ord('A'), ord('Z')-ord(n)+1)

    standard = answer
    answer += len(name)-1

    for i in range(len(name)-1):
        temp = standard + i
        checked = deepcopy(visited)
        for j in range(i+1):
            checked[j] = True
        idx = i-1

        while False in checked:
            temp += 1
            checked[idx] = True
            idx -= 1
        answer = min(answer, temp)

    for i in range(1, len(name)-1):
        temp = standard + i
        checked = deepcopy(visited)
        for j in range(1, i+1):
            checked[-j] = True
        idx = -i+1

        while False in checked:
            temp += 1
            checked[idx] = True
            idx += 1
        answer = min(answer, temp)

    return answer