# https://school.programmers.co.kr/tryouts/72119/challenges?language=python3

def solution(maps):
    answer = -1
    visited = [[False for _ in range(len(maps[i]))] for i in range(len(maps))]
    visited[0][0] = True

    queue = [[0, 0, 1]]
    x_max, y_max = len(maps)-1, len(maps[0])-1

    while queue:
        now = queue.pop(0)
        x, y, count = now[0], now[1], now[2]
        if x == x_max and y == y_max:
            answer = count
            break

        if x < x_max and maps[x+1][y] == 1 and not visited[x+1][y]:
            visited[x+1][y] = True
            queue.append([x+1, y, count+1])
        if y < y_max and maps[x][y+1] == 1 and not visited[x][y+1]:
            visited[x][y+1] = True
            queue.append([x, y+1, count+1])
        if x > 0 and maps[x-1][y] == 1 and not visited[x-1][y]:
            visited[x-1][y] = True
            queue.append([x-1, y, count+1])
        if y > 0 and maps[x][y-1] == 1 and not visited[x][y-1]:
            visited[x][y-1] = True
            queue.append([x, y-1, count+1])

    return answer