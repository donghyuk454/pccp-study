# https://school.programmers.co.kr/tryouts/72049/challenges?language=python3

def solution(n):
    answer = []

    temp_list = [[] for _ in range(n)]
    for i in range(n):
        for _ in range(i+1):
            temp_list[i].append(0)

    move = [(1, 0), (0, 1), (-1, -1)]
    move_max = [n-1, n-1, 1]
    move_num = 0
    target = n*(n+1) // 2 + 1
    now_value = 1
    x, y = 0, 0

    while now_value != target:
        temp_list[x][y] = now_value
        now_value += 1
        dx, dy = move[move_num]
        next_x = x + dx
        next_y = y + dy

        if next_x >= n or next_y >= n or temp_list[next_x][next_y] != 0:
            if move_num == 2:
                move_num = 0
            else:
                move_num += 1
            dx, dy = move[move_num]
            next_x = x + dx
            next_y = y + dy

        x, y = next_x, next_y

    for temp in temp_list:
        for t in temp:
            answer.append(t)

    return answer