import heapq
cnt = 1
while True:
    N = int(input())
    if N == 0:
        break
    Edge = dict.fromkeys(range(N**2))
    MAP = [list(map(int, input().split())) for _ in range(N)]
    delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for i in range(N):
        for j in range(N):
            Edge[i*N+j] = []
            for d in delta:
                dx = i + d[0]
                dy = j + d[1]
                if 0 <= dx < N and 0 <= dy < N:
                    Edge[i*N+j].append([MAP[dx][dy], dx*N+dy])

    pq = []
    heapq.heappush(pq, [0, 0])
    INF = int(1e9)
    distance = [INF for _ in range(N**2)]
    distance[0] = MAP[0][0]
    visit = [False for _ in range(N**2)]

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

    print("Problem "+str(cnt)+": "+str(distance[N**2-1]))
    cnt += 1

"""
다익스트라 문제
2차원 배열을 노드와 엣지의 관계로 바꾸어 다익스트라하면 된다.
다익스트라는 간선의 가중치를 이용하는것이지만
2차원 배열은 언듯 보면 간선이 아닌 정점에 가중치가 있는 모양새이기 때문에
그 이해관계를 확실히 하는것이 중요하다.

나는 N*N 배열에 순차적으로 노드 번호를 부여했다 (0, 1, 2, 3, 4, ..., N*N-1)
그리고 각 노드가 가지는 "값 K"를 "각 노드로 가기위해 필요한 가중치(weight)"로 이해했다.
그렇게 되면 각 노드가 인접한 모든 노드로 이동할 수 있는 단방향 그래프가 완성된다. (그림생략)

간성 상태를 Edge 에 저장하고 다익스트라 하는데 시작할 때 0번 노드에서 출발하기때문에
0번 노드로 갈 때 생기는 가중치를 미리 더해놓고 시작한다. ((0,0) 번 배열의 값 K = 0번 노드로 가기위해 필요한 가중치 K)

다익스트라 후
distance 의 N**2-1 번 노드를 확인하면 된다.
"""