# https://school.programmers.co.kr/tryouts/72056/challenges

def solution(s):
    answer = len(s)

    for unit in range(1, len(s)//2+1):
        temp = ""
        start = 0
        while start <= len(s)-2*unit+1:
            check = s[start:start+unit]
            count = 1
            start += unit
            while start <= len(s)-unit:
                if check != s[start:start+unit]:
                    break
                start += unit
                count += 1
            if count != 1:
                temp += str(count)
            temp += check
        temp += s[start:]
        answer = min(len(temp), answer)


    return answer