# https://school.programmers.co.kr/tryouts/72094/challenges?language=python3

def solution(n, results):
    answer = 0
    win_arr = [[] for _ in range(n+1)]
    lose_arr = [[] for _ in range(n+1)]

    for result in results:
        win_arr[result[0]].append(result[1])
        lose_arr[result[1]].append(result[0])

    for number in range(1, n+1):
        visit = [False for _ in range(n+1)]
        visit[0] = True
        queue = [number]
        while queue:
            temp_num = queue.pop(0)
            visit[temp_num] = True
            for t in win_arr[temp_num]:
                if visit[t] == False:
                    queue.append(t)

        queue = [number]
        while queue:
            temp_num = queue.pop(0)
            visit[temp_num] = True
            for t in lose_arr[temp_num]:
                if visit[t] == False:
                    queue.append(t)

        if False not in visit:
            answer += 1

    return answer