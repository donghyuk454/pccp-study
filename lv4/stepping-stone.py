# https://school.programmers.co.kr/tryouts/72078/challenges

def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    start, end = 0, distance

    while start <= end:
        mid = (start+end) // 2
        count = 0
        pre_rock = 0
        for rock in rocks:
            if rock-pre_rock < mid:
                count+=1
            else:
                pre_rock = rock
        if distance-pre_rock < mid:
            count += 1

        if count > n:
            end = mid-1
        else:
            answer = mid
            start = mid+1

    return answer