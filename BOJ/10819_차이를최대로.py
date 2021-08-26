N = int(input())
A = input().split()
visit = [0 for _ in A]
maxi = 0


def subMax(depth, result):
    if depth == N:
        global maxi
        rSum = 0
        resultList = list(map(int, result.split()))
        for i in range(len(resultList)-1):
            rSum += abs(resultList[i] - resultList[i+1])
        if maxi < rSum:
            maxi = rSum
        return

    for i in range(len(A)):
        if visit[i] == 1:
            continue

        visit[i] = 1
        subMax(depth+1, result+A[i]+" ")
        visit[i] = 0


subMax(0, "")
print(maxi)
