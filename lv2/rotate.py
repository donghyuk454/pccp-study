# https://school.programmers.co.kr/tryouts/72048/challenges?language=python3

def solution(rows, columns, queries):
    answer = []
    arr_standard = [[i*rows+j+1 for i in range(columns)] for j in range(rows)]
    arr = [[i+j*columns+1 for i in range(columns)] for j in range(rows)]
    
    for x1,y1,x2,y2 in queries:
        small_value = arr[x1-1][y1-1]
        temp1 = arr[x1-1][y1-1]
        temp2 = arr[x1-1][y1-1]
        for i in range(y1, y2):
            temp1 = temp2
            temp2 = arr[x1-1][i]
            arr[x1-1][i] = temp1
            if small_value > temp2:
                small_value = temp2
        for i in range(x1, x2-1):
            temp1 = temp2
            temp2 = arr[i][y2-1]
            arr[i][y2-1] = temp1
            if small_value > temp2:
                small_value = temp2
        for i in range(y2-1, y1-1, -1):
            temp1 = temp2
            temp2 = arr[x2-1][i]
            arr[x2-1][i] = temp1
            if small_value > temp2:
                small_value = temp2
        for i in range(x2-1, x1-1, -1):
            temp1 = temp2
            temp2 = arr[i][y1-1]
            arr[i][y1-1] = temp1
            if small_value > temp2:
                small_value = temp2
        arr[x1-1][y1-1] = temp2
        if small_value > temp2:
            small_value = temp2
        answer.append(small_value)
    
    return answer