# https://school.programmers.co.kr/tryouts/72053/challenges?language=python3

def solution(s):
    answer = ''

    for word in s.split(' '):
        for i in range(len(word)):
            if i % 2 == 0:
                answer += word[i].upper()
            else:
                answer += word[i].lower()
        answer += ' '

    return answer[:-1]