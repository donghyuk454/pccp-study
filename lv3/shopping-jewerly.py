# https://school.programmers.co.kr/tryouts/72097/challenges

def solution(gems):
    answer = [-1, -1]

    visit_cnt = dict()
    gem_kind = list(set(gems))
    start, end = 0, 0
    length = len(gems)+1

    while end < len(gems):
        if gems[end] not in visit_cnt:
            visit_cnt[gems[end]] = 0
        visit_cnt[gems[end]] += 1

        end += 1

        if len(visit_cnt) == len(gem_kind):
            while start <= end:
                if visit_cnt[gems[start]] > 1:
                    visit_cnt[gems[start]] -= 1
                    start += 1
                elif length > end-start:
                    length = end-start
                    answer = [start+1, end]
                    break
                else:
                    break

    return answer