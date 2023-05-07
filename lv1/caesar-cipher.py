# https://school.programmers.co.kr/tryouts/72052/challenges?language=python3

def solution(s, n):
    answer = ''

    for cha in s:
        if cha == ' ':
            answer += cha
            continue
        value = ord(cha)
        if value >= ord('a'):
            value += n
            if value > ord('z'):
                value = value - ord('z') + ord('a') - 1
        else:
            value += n
            if value > ord('Z'):
                value = value - ord('Z') + ord('A') - 1
        answer += chr(value)

    return answer