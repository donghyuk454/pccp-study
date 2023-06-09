# https://school.programmers.co.kr/tryouts/72059/challenges?language=python3

def solution(new_id):
    answer = ''
    # level 1
    temp1 = new_id.lower()

    # level 2
    temp2 = ''
    for t in temp1:
        if ord(t) >= ord('a') and ord(t) <= ord('z'):
            temp2 += t
            continue
        if ord(t) >= ord('0') and ord(t) <= ord('9'):
            temp2 += t
            continue
        if t == '-' or t == '_' or t == '.':
            temp2 += t

    # level 3
    i = 0
    while i < len(temp2):
        if temp2[i] == '.':
            answer += temp2[i]
            if i == len(temp2)-1:
                i += 1
                continue
            if temp2[i+1] != '.':
                i += 1
                continue
            j = i+1
            while j < len(temp2):
                if temp2[j] != '.':
                    break
                j += 1
            i = j
            continue
        answer += temp2[i]
        i += 1

    # level 4
    if len(answer) > 0 and answer[0] == '.':
        answer = answer[1:]
    if len(answer) > 0 and answer[-1] == '.':
        answer = answer[:-1]

    # level 5
    if answer == "":
        answer = "a"

    # level 6
    if len(answer) >= 16:
        answer = answer[:15]
    if len(answer) > 0 and answer[-1] == '.':
        answer = answer[:-1]

    # level 7
    if len(answer) == 1:
        answer += answer[-1]
        answer += answer[-1]
    elif len(answer) == 2:
        answer += answer[-1]

    return answer