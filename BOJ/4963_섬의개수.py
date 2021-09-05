import sys

delta = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, 1], [-1, -1], [1, 1], [1, -1]]

while True:
    W, H = map(int, sys.stdin.readline().split())
    if W == 0 and H == 0:
        break
    MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]
    visit = [[False for _ in range(W)] for _ in range(H)]
    q = []
    cnt = 0

    for i in range(H):
        for j in range(W):
            if visit[i][j] or MAP[i][j] == 0:
                continue

            visit[i][j] = True
            q.append([i, j])

            while len(q) != 0:
                n = q.pop(0)

                for d in delta:

                    dx = n[0] + d[0]
                    dy = n[1] + d[1]

                    if 0 <= dx < H and 0 <= dy < W and MAP[dx][dy] == 1 and not visit[dx][dy]:
                        visit[dx][dy] = True
                        q.append([dx, dy])

            cnt += 1

    print(cnt)
