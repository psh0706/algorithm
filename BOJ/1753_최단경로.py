import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
Edge = dict.fromkeys(range(V+1))
INF = int(1e9)
distance = [INF for _ in range(V+1)]

for _ in range(E):
    s, e, w = map(int, sys.stdin.readline().split())
    if Edge[s]:
        Edge[s].append([w, e])
    else:
        Edge[s] = [[w, e]]

for e in Edge:
    if not Edge[e]:
        Edge[e] = []

pq = []
heapq.heappush(pq, [0, start])
distance[start] = 0
visit = [False for _ in range(V+1)]

while len(pq) != 0:
    now = heapq.heappop(pq)

    v = now[1]
    v_dist = distance[now[1]] # 이부분이 중요하다.
    """
    단순히 간선의 가중치가 아닌, 시작 정점으로부터 해당 노드까지의 최단거리를 가져와야한다. 
    distance 에 기록되어있다. 프림과의 차이점
    """
    if visit[v]:
        continue
    visit[v] = True

    for e in Edge[v]:
        ve_dist = e[0]
        dist = v_dist + ve_dist

        if distance[e[1]] > dist:
            distance[e[1]] = dist
            heapq.heappush(pq, [dist, e[1]])
            """
            우선순위 큐에 넣는 경우는 지금 기록된 최단거리보다 더 작은 거리를 발견했을 때 이므로 갱신된 dist 값을 넣어준다.
            """


for d in range(1, len(distance)):
    if distance[d] == INF:
        print('INF')
        continue
    print(distance[d])


"""
다익스트라를 이해하고 처음 풀어본 기본 of 기본 문제
프림 알고리즘이랑 비슷한듯 하지만 다르다
프림이나 크루스칼이 모든 경로 중 가장 cost 가 적은 경로를 찾는 알고리즘이라면
다익스트라는 어떤 한 정점에서부터 다른 정점들까지의 최단경로를 찾는 알고리즘이다.
우선순위 큐를 이용해 코스트가 적은 순서대로 노드를 뽑고,
그 노드를 기준으로 최단경로 정보를 가지는 배열을 계속 갱신해 나간다.
아주 기본적인 문제였지만 이해하는 데에 시간을 들이느랴 전체적으로 해결 시간이 걸렸던 문제.
다익스트라를 이해하고 나니 대충 어떤식으로 문제에 이용될지 머릿속으로 그려진다
앞으로 다익스트라를 활용한 알고리즘들을 많이 풀어보고싶다!
"""