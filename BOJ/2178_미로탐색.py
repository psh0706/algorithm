import heapq

m, n = map(int, input().split())
MAP = [list(map(int, list(input()))) for _ in range(m)]
visit = [[False for _ in range(n)] for _ in range(m)]
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]

q = []

# [이동, x, y] -> 이동거리를 이용한 우선순위큐.
heapq.heappush(q, [1, 0, 0])
visit[0][0] = True

while q:
    [move, x, y] = heapq.heappop(q)

    if x+1 == m and y+1 == n:
        print(move)
        break

    for d in delta:
        dx = x + d[0]
        dy = y + d[1]

        if 0 <= dx < m and 0 <= dy < n and not visit[dx][dy]:
            if MAP[dx][dy] == 1:
                visit[dx][dy] = True
                q.append([move+1, dx, dy])


"""
bfs + 최단거리 => 우선순위 큐를 쓴 bfs
큐에서 하나를 뽑을 때, 이동거리를 이용해 우선순위큐를 사용하면 
별도의 방문처리에 힘을 줄 필요 없이 목적지까지 가장 빠르게 가는 루트를 알아낼수 있다.
"""