# https://school.programmers.co.kr/tryouts/72112/challenges?language=python3https://school.programmers.co.kr/tryouts/72112/challenges?language=python3

def solution(skill, skill_trees):
    answer = 0
    must_before_skill = dict()
    for i in range(ord('A'), ord('Z')+1):
        must_before_skill[chr(i)] = ""

    must_before_skill[skill[0]] = "start"
    for i in range(1, len(skill)):
        must_before_skill[skill[i]] = skill[i-1]

    for skill_tree in skill_trees:
        before_skill = "start"
        is_countable = True
        for s in skill_tree:
            if must_before_skill[s] == "":
                continue
            if must_before_skill[s] != before_skill:
                is_countable = False
                break
            before_skill = s
        if is_countable:
            answer += 1

    return answer