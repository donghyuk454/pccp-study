# https://school.programmers.co.kr/tryouts/72070/challenges

from copy import deepcopy

def solution(user_id, banned_id):
    answer = 0
    ban_candidates = dict()

    for ban in banned_id:
        if ban in ban_candidates:
            continue
        ban_candidates[ban] = []
        for user in user_id:
            if check_is_candidate(ban, user):
                ban_candidates[ban].append(user)

    def find(visited, ban_idx, route):
        if ban_idx == len(banned_id):
            return [route]

        candidates = ban_candidates[banned_id[ban_idx]]
        result = []
        for cand in candidates:
            if visited[cand]:
                continue
            new_visited = deepcopy(visited)
            new_visited[cand] = True
            new_route = deepcopy(route)
            new_route.append(cand)
            result += find(new_visited, ban_idx+1, new_route)

        return result

    new_visited = dict()
    for user in user_id:
        new_visited[user] = False
    result = find(new_visited, 0, [])

    for i in range(len(result)):
        result[i].sort()
    temp = []
    for r in result:
        route_str = ""
        for i in r:
            route_str += i
        temp.append(route_str)

    answer = len(list(set(temp)))

    return answer

def check_is_candidate(ban, user):
    if len(user) != len(ban):
        return False

    for i in range(len(ban)):
        if ban[i] == '*':
            continue
        if user[i] != ban[i]:
            return False
    return True

def check_is_same(v1, v2):
    for u in v1:
        if v1[u] != v2[u]:
            return False
    return True
