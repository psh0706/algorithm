def solution(N, stages):
    failed = [[] for _ in range(N+1)]
    userNum = len(stages)

    for i in range(1, len(failed)):
        failUser = stages.count(i)
        ratio = 0 if userNum == 0 else failUser/userNum
        failed[i] = [ratio, i]
        userNum -= failUser

    failed.pop(0)
    failed.sort(key=lambda x: (-x[0], x[1]))
    answer = [i[1] for i in failed]
    return answer