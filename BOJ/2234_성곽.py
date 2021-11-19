N, M = map(int, input().split())
walls = [list(map(bin, map(int, input().split()))) for _ in range(M)]
outOfWalls = [[[] for _ in range(N)] for _ in range(M)]
MAP = [[0 for _ in range(N)] for _ in range(M)]
delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
rooms = []


for i in range(M):
    for j in range(N):
        walls[i][j] = walls[i][j][2:].zfill(4)
        for d in range(4):
            if walls[i][j][d] == '0':
                outOfWalls[i][j].append(delta[d])


visit = [[False for _ in range(N)] for _ in range(M)]
num = 0
for i in range(M):
    for j in range(N):
        if visit[i][j]:
            continue
        q = [[i, j]]
        MAP[i][j] = num
        visit[i][j] = True
        cnt = 1
        while q:
            n = q.pop(0)
            for d in outOfWalls[n[0]][n[1]]:
                dx = n[0] + d[0]
                dy = n[1] + d[1]
                if visit[dx][dy]:
                    continue
                visit[dx][dy] = True
                q.append([dx, dy])
                MAP[dx][dy] = num
                cnt += 1
        rooms.append(cnt)
        num += 1


adj = [[] for _ in range(len(rooms))]
visit = [[False for _ in range(N)] for _ in range(M)]
for i in range(M):
    for j in range(N):
        if visit[i][j]:
            continue
        q = [[i, j]]
        visit[i][j] = True
        num = MAP[i][j]
        while q:
            n = q.pop(0)
            for d in delta:
                dx = n[0] + d[0]
                dy = n[1] + d[1]

                if 0 <= dx < M and 0 <= dy < N :
                    if MAP[dx][dy] != num:
                        adj[num].append(MAP[dx][dy])
                    else:
                        if not visit[dx][dy]:
                            visit[dx][dy] = True
                            q.append([dx, dy])

maxi = 0
for k in range(len(adj)):
    temp = list(set(adj[k]))
    for t in temp:
        maxi = max(maxi, rooms[k] + rooms[t])


print(len(rooms))
print(max(rooms))
print(maxi)

"""
bfs 로 접근해서 풀어보았다.
아래 세 개를 구해야했는데

1. 이 성에 있는 방의 개수
2. 가장 넓은 방의 넓이
3. 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기

각 영역을 파악하니 1번과 2번은 해결이 되었다. (rooms)
문제는 3번이었는데
인접한 방을 알아낼까, 벽을 하나씩 지우면서 bfs 해볼까 고민하다
아무래도 전자가 더 빠른 시간복잡도를 가질것 같아 그렇게 구현했다. (adj)
인접한 두방의 크기를 더한것 중 가장 큰 값을 구해 3을 해결하였다.
"""

