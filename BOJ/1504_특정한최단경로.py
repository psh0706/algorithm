import sys
import heapq

N, E = map(int, sys.stdin.readline().split())
Edge = dict.fromkeys(range(N+1))
for e in Edge:
    Edge[e] = []

for _ in range(E):
    s, e, w = map(int, sys.stdin.readline().split())
    Edge[s].append([w, e])
    Edge[e].append([w, s])


v1, v2 = map(int, sys.stdin.readline().split())

INF = int(1e9)
distanceTable = {
    1: [INF for _ in range(N+1)],
    v1: [INF for _ in range(N+1)],
    v2: [INF for _ in range(N+1)]
}


def dijkstra(start):

    pq = []
    heapq.heappush(pq, [0, start])
    distanceTable[start][start] = 0
    visit = [False for _ in range(N+1)]

    while pq:
        now = heapq.heappop(pq)

        v = now[1]
        v_dist = distanceTable[start][now[1]]

        if visit[v]:
            continue
        visit[v] = True

        for e in Edge[v]:
            ve_dist = e[0]
            dist = v_dist + ve_dist

            if distanceTable[start][e[1]] > dist:
                distanceTable[start][e[1]] = dist
                heapq.heappush(pq, [dist, e[1]])


dijkstra(1)
dijkstra(v1)
dijkstra(v2)

case1 = distanceTable[1][v1]+distanceTable[v1][v2]+distanceTable[v2][N]
case2 = distanceTable[1][v2]+distanceTable[v2][v1]+distanceTable[v1][N]

if case2 >= INF and case1 >= INF:
    print(-1)
else:
    if case1 >= case2:
        print(case2)
    else:
        print(case1)
