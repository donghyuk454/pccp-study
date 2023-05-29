# https://school.programmers.co.kr/tryouts/72110/challenges?language=python3

def solution(numbers, hand):
    answer = ''
    phone = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -1]]
    position = dict()
    for i in range(len(phone)):
        for j in range(len(phone[0])):
            position[phone[i][j]] = (i, j)

    left = [3, 0]
    right = [3, 2]
    left_number = [1, 4, 7]
    right_number = [3, 6, 9]

    for number in numbers:
        x, y = position[number]

        if number in left_number:
            left = [x, y]
            answer += "L"
            continue
        if number in right_number:
            right = [x, y]
            answer += "R"
            continue

        dist_left = abs(x-left[0]) + abs(y-left[1])
        dist_right = abs(x-right[0]) + abs(y-right[1])
        if dist_left == dist_right:
            if hand == "left":
                left = [x, y]
                answer += "L"
            else:
                right = [x, y]
                answer += "R"
        elif dist_left < dist_right:
            left = [x, y]
            answer += "L"
        else:
            right = [x, y]
            answer += "R"

    return answer