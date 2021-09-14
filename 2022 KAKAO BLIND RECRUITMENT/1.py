id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3


def solution(id_list, report, k):
    reportDict, reportedDict = dict.fromkeys(id_list), dict.fromkeys(id_list)
    answer = [0 for _ in range(len(id_list))]
    reportedID = []

    for id in id_list:
        reportDict[id] = []
        reportedDict[id] = 0

    for r in report:
        a, b = r.split()
        if b not in reportDict[a]:
            reportDict[a].append(b)

    for i in reportDict:
        for j in range(len(reportDict[i])):
            reportedDict[reportDict[i][j]] += 1

    for rd in reportedDict:
        if reportedDict[rd] >= k:
            reportedID.append(rd)

    for reported in reportedID:
        for i in reportDict:
            if reported in reportDict[i]:
                answer[id_list.index(i)] += 1

    print(answer)

    return answer


solution(id_list, report, k)