# https://school.programmers.co.kr/tryouts/72093/challenges?language=python3

def solution(n, edge):
    answer = 0
    visited = [False for _ in range(n+1)]
    visited[0] = True

    tree = dict()
    for i in range(1, n+1):
        tree[i] = []

    for e in edge:
        tree[e[0]].append(e[1])
        tree[e[1]].append(e[0])

    now = [1]
    while False in visited:
        for n in now:
            visited[n] = True

        new_now = []
        for n in now:
            for i in range(len(tree[n])):
                if visited[tree[n][i]] or tree[n][i] in new_now:
                    continue
                new_now.append(tree[n][i])
        if len(new_now) > 0:
            now = new_now

    answer = len(now)

    return answer