def solution(n, info):
    apeach = dict.fromkeys(range(10, -1, -1))
    apeachScore = 0
    caseList = []

    for i in range(len(info)):
        if info[i] != 0:
            apeachScore += 10 - i
        apeach[10 - i] = info[i]

    def recursion(depth, start, result):
        if depth == 0:
            rList = result.split()
            temp = [0 for _ in range(11)]
            for r in rList:
                s, lionScore = map(int, r.split(":"))
                temp[10 - s] = lionScore
            caseList.append(temp)
            return

        for score in range(start, -1, -1):
            lion = apeach[score] + 1

            if depth - lion < 0:
                continue

            # 이부분 수정 필요함
            if score == 0:
                lion = depth
            else:
                lion = apeach[score] + 1

            nextDepth = depth - lion
            recursion(nextDepth, start - 1, result + str(score) + ":" + str(lion) + " ")

    recursion(n, 10, '')

    aList = [0 for _ in range(len(caseList))]
    for i in range(len(caseList)):
        case = caseList[i]
        l = 0
        a = 0

        for j in range(11):
            if apeach[10 - j] < case[j]:
                l += 10 - j
            elif apeach[10 - j] > case[j]:
                a += 10 - j
            else:
                continue

        aList[i] = l - a

    maxi = max(aList)

    if max(aList) <= 0:
        answer = [-1]
    else:
        answerIndex = 0
        for i in range(len(aList)):
            if aList[i] == maxi:
                answerIndex = i

        answer = caseList[answerIndex]

    print(answer)
    return answer


solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3])
