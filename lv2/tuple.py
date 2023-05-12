# https://school.programmers.co.kr/tryouts/72054/challenges?language=python3

def solution(s):
    answer = []
    splited_s = s[1:-1].split("},")

    for i in range(len(splited_s)):
        splited_s[i] = splited_s[i][1:]
        if splited_s[i][-1] == "}":
            splited_s[i] = splited_s[i][:-1]
        splited_s[i] = splited_s[i].split(",")
        splited_s[i] = list(map(int, splited_s[i]))

    splited_s.sort(key = lambda x:len(x))

    for ss in splited_s:
        for sss in ss:
            if sss not in answer:
                answer.append(sss)
                break

    return answer