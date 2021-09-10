import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
Edge = dict.fromkeys(range(N+1))

for _ in range(M):
    start, end, weight = map(int, sys.stdin.readline().split())
    if Edge[start]:
        Edge[start].append([weight, end])
    else:
        Edge[start] = [[weight, end]]

    if Edge[end]:
        Edge[end].append([weight, start])
    else:
        Edge[end] = [[weight, start]]


pq = []
heapq.heappush(pq, [0, 1])
visit = [False for _ in range(N+1)]
acc = 0
cnt = 0

while len(pq) != 0:
    if cnt == N:
        break

    now = heapq.heappop(pq)

    v = now[1]
    if visit[v]:
        continue
    visit[v] = True

    w = now[0]
    cnt += 1
    acc += w

    for e in Edge[v]:
        if visit[e[1]]:
            continue
        else:
            heapq.heappush(pq, e)

print(acc)
