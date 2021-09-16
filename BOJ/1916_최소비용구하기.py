import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

Edge = dict.fromkeys(range(N+1))
INF = int(1e9)
distance = [INF for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, sys.stdin.readline().split())
    if Edge[s]:
        Edge[s].append([w, e])
    else:
        Edge[s] = [[w, e]]
for e in Edge:
    if not Edge[e]:
        Edge[e] = []

nodeS, nodeE = map(int, sys.stdin.readline().split())

pq = []
heapq.heappush(pq, [0, nodeS])
distance[nodeS] = 0
visit = [False for _ in range(N+1)]
while len(pq) != 0:
    now = heapq.heappop(pq)

    v = now[1]
    v_dist = distance[now[1]]

    if visit[v]:
        continue
    visit[v] = True

    for e in Edge[v]:
        ve_dist = e[0]
        dist = v_dist + ve_dist

        if distance[e[1]] > dist:
            distance[e[1]] = dist
            heapq.heappush(pq, [dist, e[1]])

print(distance[nodeE])

"""
지정된 출발지로 다익스트라 해서 모든 정점으로의 최단거리를 구한 뒤,
지정된 도착지의 최단거리를 출력하면 되는 문제
거의 기본 다익스트라 구현이고 개념자체를 이해했다면 엄청 쉬운문제
"""