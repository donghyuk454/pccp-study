# https://school.programmers.co.kr/tryouts/72050/challenges?language=python3

def solution(places):
    answer = []

    for place in places:
        for x in range(len(place)):
            is_ok = True
            for y in range(len(place)):
                if place[x][y] == 'P' and not find_is_ok(place, x, y, 2, True):
                    print(x, y)
                    is_ok = False
                    break
            if not is_ok:
                break
        if is_ok:
            answer.append(1)
            continue
        answer.append(0)

    return answer

def find_is_ok (place, x, y, count, is_down):
    if count < 0 or x < 0 or x >= len(place) or y < 0 or y >= len(place) or place[x][y] == 'X':
        return True

    if count != 2 and place[x][y] == 'P':
        return False

    results = []

    results.append(find_is_ok(place, x+1, y, count-1, True))
    results.append(find_is_ok(place, x, y+1, count-1, False))

    if count == 2 and (y>0 and place[x][y-1] == 'O') and (x<4 and place[x+1][y-1] == 'P'):
        results.append(False)

    if count == 1:
        if is_down:
            results.append(find_is_ok(place, x, y-1, count-1, is_down))
        else:
            results.append(find_is_ok(place, x-1, y, count-1, is_down))

    return False not in results