# https://school.programmers.co.kr/tryouts/72084/challenges?language=python3

def solution(record):
    answer = []
    uid_name = dict()

    for r in record:
        action = r.split(" ")
        uid = action[1]
        if action[0] == "Enter":
            uid_name[uid] = action[2]
            answer.append(uid+"님이 들어왔습니다.")
        elif action[0] == "Leave":
            answer.append(uid+"님이 나갔습니다.")
        elif action[0] == "Change":
            uid_name[uid] = action[2]

    for i in range(len(answer)):
        uid = answer[i].split("님")[0]
        answer[i] = answer[i].replace(uid, uid_name[uid])

    return answer