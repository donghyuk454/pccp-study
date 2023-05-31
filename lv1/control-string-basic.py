# https://school.programmers.co.kr/tryouts/72060/challenges?language=python3

def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False

    for c in s:
        if ord(c) < ord('0') or ord(c) > ord('9'):
            return False

    return True