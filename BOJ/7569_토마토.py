from collections import deque


def solution():
    C, R, H = map(int, input().split())
    visit = [[[False for _ in range(C)] for _ in range(R)] for _ in range(H)]
    delta = [[1, 0, 0], [0, 1, 0], [-1, 0, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
    ripes = deque()
    unripe = 0
    box = []
    for i in range(H):
        box.append([])
        for j in range(R):
            line = list(map(int, input().split()))
            for k in range(C):
                if line[k] == -1 or line[k] == 1:
                    if line[k] == 1:
                        ripes.append([j, k, i])
                    visit[i][j][k] = True
                else:
                    unripe += 1
            box[i].append(line)

    cnt = 0
    while ripes:
        size = len(ripes)
        cnt += 1
        for _ in range(size):
            tomato = ripes.popleft()
            for d in delta:
                dx = tomato[0] + d[0]
                dy = tomato[1] + d[1]
                dz = tomato[2] + d[2]
                if 0 <= dx < R and 0 <= dy < C and 0 <= dz < H and not visit[dz][dx][dy]:
                    visit[dz][dx][dy] = True
                    ripes.append([dx, dy, dz])
                    unripe -= 1

    if unripe == 0:
        print(cnt - 1)
    else:
        print(-1)


solution()

"""
7576 토마토 문제와 같은 문제
2차원 -> 3차원 으로 변경
"""
