import sys

M, N = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
visit = [[False for _ in range(M)] for _ in range(N)]
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
q = []
arrival = 0

visit[0][0] = True
q.append([0, 0, 0])

while len(q) != 0:
    size = len(q)
    for _ in range(size):
        n = q.pop(0)

        if (n[0] + 1) == N and (n[1] + 1) == M:
            arrival = n[2]

        for d in delta:
            dx = n[0] + d[0]
            dy = n[1] + d[1]
            brokenWall = n[2]

            if 0 <= dx < N and 0 <= dy < M and not visit[dx][dy]:
                if MAP[dx][dy] == 1:
                    brokenWall += 1
                    visit[dx][dy] = True
                    q.append([dx, dy, brokenWall])
                else:
                    visit[dx][dy] = True
                    q.insert(0, [dx, dy, brokenWall])

print(arrival)


# 처음에는 상태를 저장하는것으로 구현 (우선순위 큐 방식)
# 후에 0-1 BFS 알고리즘으로 구현
