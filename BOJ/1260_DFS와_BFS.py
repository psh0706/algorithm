import sys

N, M, V = map(int, sys.stdin.readline().split())
connectionInfo = [[] for _ in range(N+1)]
visit = [False for _ in range(N+1)]
dfsResult = ''
bfsQueue = list()

for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    connectionInfo[start].append(end)
    connectionInfo[end].append(start)

for a in connectionInfo:
    if len(a) == 0:
        continue
    a.sort()


# dfs 실행
def dfs(node):
    global dfsResult

    if visit[node]:
        return

    visit[node] = True
    dfsResult += str(node) + " "

    for nextNode in connectionInfo[node]:
        dfs(nextNode)


dfs(V)
print(dfsResult)
visit = [False for _ in range(N+1)]

# bfs 실행
bfsResult = ''
visit[V] = True
bfsQueue.append(V)

while len(bfsQueue) != 0:

    node = bfsQueue.pop(0)
    bfsResult += str(node) + " "

    for nextNode in connectionInfo[node]:
        if visit[nextNode]:
            continue
        visit[nextNode] = True
        bfsQueue.append(nextNode)


print(bfsResult)
