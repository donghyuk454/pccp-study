# https://school.programmers.co.kr/tryouts/72077/challenges

def solution(info, query):
    answer = []

    developers = dict()

    for i in info:
        contents = i.split(" ")
        temp = []
        for i in range(len(contents)-1):
            temp.append([contents[i], "-"])
        add_list = get_add_list(temp)
        for add in add_list:
            if add not in developers:
                developers[add] = []
            value = int(contents[-1])
            developers[add].append(value)

    for key in developers.keys():
        developers[key].sort()

    for q in query:
        key, number = find_key_number(q)
        if key not in developers:
            answer.append(0)
            continue
        s = 0
        e = len(developers[key])-1
        m = 0
        while s <= e:
            m = (s+e) // 2
            if developers[key][m] < number:
                s = m+1
            elif developers[key][m] > number:
                e = m-1
            else:
                while m >= 0 and developers[key][m] == number:
                    m -= 1
                m += 1
                break
        if developers[key][m] < number:
            m += 1
        answer.append(len(developers[key])-m)

    return answer

def get_add_list(temp):
    add_list = []
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for w in range(2):
                    add_list.append(temp[0][i]+temp[1][j]+temp[2][k]+temp[3][w])
    return add_list

def find_key_number(query_line):
    splited = query_line.split(" ")
    number = int(splited[-1])
    key = splited[0] + splited[2] + splited[4] + splited[6]
    return key, number