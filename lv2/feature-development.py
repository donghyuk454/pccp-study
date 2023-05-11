# https://school.programmers.co.kr/tryouts/72092/challenges?language=python3

def solution(progresses, speeds):
    answer = []
    remain_days = [ ((100-progresses[i]) // speeds[i]) for i in range(len(progresses))]

    for i in range(len(remain_days)):
        if (100-progresses[i])%speeds[i] != 0:
            remain_days[i] += 1

    while remain_days:
        now_day = remain_days.pop(0)
        release_count = 1

        while remain_days:
            if remain_days[0] > now_day:
                break
            remain_days.pop(0)
            release_count += 1

        answer.append(release_count)

    return answer