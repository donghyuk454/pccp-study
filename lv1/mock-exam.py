# https://school.programmers.co.kr/tryouts/72067/challenges?language=python3

def solution(answers):
    answer = []
    persons = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    correct_count = [0,0,0]

    for i in range(len(persons)):
        length = len(persons[i])
        for j in range(len(answers)):
            if answers[j] == persons[i][j % length]:
                correct_count[i] += 1

    max_count = max(correct_count)
    for i in range(len(correct_count)):
        if correct_count[i] == max_count:
            answer.append(i+1)

    return answer