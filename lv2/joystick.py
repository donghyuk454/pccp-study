# https://school.programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    answer = 0
    if set(name) == {'A'}:
        return 0

    answer = float('inf')
    for i in range(len(name) // 2):
        left_moved = name[-i:]+name[:-i]
        right_moved = name[i:]+name[:i]
        for n in [left_moved, right_moved[0]+right_moved[:0:-1]]:
            while n and n[-1] == 'A':
                n = n[:-1]

            row_move = i + len(n)-1
            col_move = 0
            for c in map(ord, n):
                col_move += min(c - ord('A'), ord('Z') + 1 - c)

            answer = min(answer, row_move + col_move)
    return answer