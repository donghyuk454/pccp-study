# https://school.programmers.co.kr/tryouts/72062/challenges?language=python3

def solution(num):
    if num == 0:
        return 0

    def find(number, count):
        if number == 1:
            return count
        if count == 501:
            return -1

        if number % 2 == 0:
            return find(number//2, count+1)
        return find(number*3+1, count+1)

    answer = find(num, 0)

    return answer