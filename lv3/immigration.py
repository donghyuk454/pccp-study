# https://school.programmers.co.kr/tryouts/72076/challenges?language=python3

def solution(n, times):
    answer = 0

    left, right = 1, max(times)*n

    while left <= right:
        mid = left + (right - left) // 2
        count = 0
        for t in times:
            count += mid // t

        if count >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1


    return answer