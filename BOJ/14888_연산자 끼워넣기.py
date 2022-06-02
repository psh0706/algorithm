n = int(input())
arr = list(map(int, input().split()))
opCount = list(map(int, input().split()))
visit = [0 for _ in range(4)]
minAns = 10000000000
maxAns = -10000000000


def calc(a, b, op):
    if op == 0:
        return a + b
    elif op == 1:
        return a - b
    elif op == 2:
        return a * b
    else:
        return int(a/b)


def dfs(depth, value, oplist):
    global minAns, maxAns

    if depth == n - 1:
        if minAns > value:
            minAns = min(minAns, value)
        if maxAns < value:
            maxAns = max(maxAns, value)
        return

    for i in range(4):
        if visit[i] == opCount[i]:
            continue

        visit[i] += 1
        temp = arr[depth+1]
        dfs(depth + 1, calc(value, temp, i), oplist+str(i))
        visit[i] -= 1


dfs(0, arr[0], "")
print(maxAns)
print(minAns)

"""
dfs 를 이용한 완탐 문제
"""