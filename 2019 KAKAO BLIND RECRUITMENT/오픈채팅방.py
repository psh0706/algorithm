def solution(record):
    answer = []
    user = {}
    roomLogs = []

    for r in record:
        r = r.split()
        log = r[0]
        userID = r[1]
        nickName = r[2] if len(r) == 3 else ''

        if log == "Enter":
            user[userID] = nickName
            roomLogs.append([log, userID])

        elif log == "Change":
            user[userID] = nickName

        elif r[0] == "Leave":
            roomLogs.append([log, userID])

    for roomLog in roomLogs:
        log = roomLog[0]
        userID = roomLog[1]

        if log == "Enter":
            answer.append(user[userID] + "님이 들어왔습니다.")
        elif log == "Leave":
            answer.append(user[userID] + "님이 나갔습니다.")

    return answer

