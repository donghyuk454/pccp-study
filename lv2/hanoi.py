# https://school.programmers.co.kr/tryouts/72063/challenges

def solution(n):
    answer = []

    def hanoi(start, end, inter, n):
        if n == 1:
            answer.append([start, end])
            return
        # 시작기둥의 n-1 개 원판을 중간다리 기둥으로 옮긴다
        hanoi(start,inter,end,n-1)
        # 시작기둥의 남은 하나의 원판을 목표기둥으로 옮긴다
        hanoi(start,end,inter,1)
        # n-1 개의 원판을 중간다리를 시작기둥으로, 시작기둥을 중간다리 기둥으로 사용해 옳긴다
        hanoi(inter,end,start,n-1)

    hanoi(1,3,2,n)

    return answer

