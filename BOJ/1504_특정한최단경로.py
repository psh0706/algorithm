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


"""
다익스트라 응용 문제
1번 정점~ N번 정점 까지의 최단 경로 중 특정한 두 정점 (v1, v2) 를 지나는 최단경로를 찾는 문제이다.

1번 정점부터 시작하고 (start) N번 정점에서 끝나야하므로 (end) 최단 경로로는 두 가지 경우의 수가 존재한다.

case 1) 
    start - v1 - v2 - end
    => start 부터 v1 까지의 최단경로 + v1 부터 v2 까지의 최단경로 + v2 부터 end 까지의 최단경로
    
case 2)
    start - v2 - v1 - end
    => start 부터 v2 까지의 최단경로 + v2 부터 v1 까지의 최단경로 + v1 부터 end 까지의 최단경로
    
따라서 start 로 시작하는 다익스트라,
v1 으로 시작하는 다익스트라,
v2 로 시작하는 다익스트라 를 구하면 모든 경우에 대응할 수 있다. 
(본 구현 에서는 세 가지 다익스트라를 딕셔너리(해시맵) 으로 엮어 주었다.)

두 가지 경우 중 더 작은 weight 를 가지는것을 출력하면 된다.
"""