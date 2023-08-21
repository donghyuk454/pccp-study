# https://school.programmers.co.kr/tryouts/72096/challenges?language=python3

def solution(jobs):
    answer = 0
    jobs.sort()
    queue = jobs[:]
    value = 0
    now_time = 0
    min_idx = 0
    while queue:
        now_idx = 0
        min_value = float('inf')
        while now_idx < len(queue) and queue[now_idx][0] <= now_time:
            if min_value > queue[now_idx][1]:
                min_idx = now_idx
                min_value = queue[now_idx][1]
            now_idx += 1
        if min_value == float('inf'):
            now_time += 1
            continue
        value += now_time - queue[min_idx][0] + min_value
        now_time += min_value
        queue.pop(min_idx)

    answer = value // len(jobs)


    return answer