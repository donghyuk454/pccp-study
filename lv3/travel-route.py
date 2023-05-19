# https://school.programmers.co.kr/tryouts/72115/challenges?language=python3

import copy

def solution(tickets):
    answer = []
    meta_roads = {}

    for ticket in tickets:
        if ticket[0] not in meta_roads:
            meta_roads[ticket[0]] = [ticket[1]]
        else:
            meta_roads[ticket[0]].append(ticket[1])
            meta_roads[ticket[0]].sort()

        if ticket[1] not in meta_roads:
            meta_roads[ticket[1]] = []

    end_count = len(tickets) + 1

    def dfs(city, roads, route):
        if len(route) == end_count:
            return route

        for next_city in roads[city]:
            new_roads = copy.deepcopy(roads)
            new_roads[city].remove(next_city)
            new_route = copy.deepcopy(route)
            new_route.append(next_city)
            result = bfs(next_city, new_roads, new_route)
            if len(result) > 0:
                return result

        return []

    answer = dfs("ICN", meta_roads, ["ICN"])

    return answer