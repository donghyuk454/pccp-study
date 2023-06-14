# https://school.programmers.co.kr/tryouts/72118/challenges?language=python3

from copy import deepcopy

def solution(begin, target, words):
    if target not in words:
        return 0

    queue = [[begin, 0, [False for _ in range(len(words))]]]

    while queue:
        now = queue.pop(0)
        value = now[0]
        count = now[1]
        visited = now[2]

        if value == target:
            return count

        for i in range(len(words)):
            if visited[i]:
                continue
            if dif_count(value, words[i]) == 1:
                new_visited = deepcopy(now[2])
                new_visited[i] = True
                queue.append([words[i], count+1, new_visited])

    return 0

def dif_count(str1, str2):
    result = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            result += 1
    return result