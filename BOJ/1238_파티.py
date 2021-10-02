import sys
import heapq

N, E, X = map(int, sys.stdin.readline().split())
Edge = dict.fromkeys(range(N+1))
rvsEdge = dict.fromkeys(range(N+1))
for e in Edge:
    Edge[e] = []
    rvsEdge[e] = []

for _ in range(E):
    s, e, w = map(int, sys.stdin.readline().split())
    Edge[s].append([w, e])
    rvsEdge[e].append([w, s])

INF = int(1e9)
toX = [INF for _ in range(N+1)]
fromX = [INF for _ in range(N+1)]
answer = [0 for _ in range(N+1)]


def dijkstra_to_x(start):
    pq = []
    heapq.heappush(pq, [0, start])
    toX[start] = 0
    visit = [False for _ in range(N+1)]

    while pq:
        now = heapq.heappop(pq)

        v = now[1]
        if visit[v]:
            continue
        visit[v] = True

        v_dist = toX[now[1]]

        for e in Edge[v]:
            ve_dist = e[0]
            dist = v_dist + ve_dist

            if toX[e[1]] > dist:
                toX[e[1]] = dist
                heapq.heappush(pq, [dist, e[1]])


def dijkstra_from_x(start):
    pq = []
    heapq.heappush(pq, [0, start])
    fromX[start] = 0
    visit = [False for _ in range(N+1)]

    while pq:
        now = heapq.heappop(pq)

        v = now[1]
        if visit[v]:
            continue
        visit[v] = True

        v_dist = fromX[now[1]]

        for e in rvsEdge[v]:
            ve_dist = e[0]
            dist = v_dist + ve_dist

            if fromX[e[1]] > dist:
                fromX[e[1]] = dist
                heapq.heappush(pq, [dist, e[1]])


dijkstra_to_x(X)
dijkstra_from_x(X)

for i in range(1, N+1):
    answer[i] += toX[i]
    answer[i] += fromX[i]

print(max(answer))


"""
처음 문제를 풀었을 때는 1~N 까지의 노드에 시작하는 다익스트라를 전부 구해서 X의 최단거리를 구하고
X노드에서 시작하는 다익스트라를 구해서 각 노드로 가는 최단거리들을 더해주었는데 (1880ms)
모든 노드 -> X번 노드로 가는 최단거리를 그래프를 뒤집어서 다익스트라 함으로 쓸데없이 N번 다익스트라를 하지 않아도
단 두번만에 정답을 구할수 있었다 (92ms)
"""