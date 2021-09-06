import sys

R, C = map(int, sys.stdin.readline().split())
pan = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
visit = [[False for _ in range(C)] for _ in range(R)]
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
q = []
melt = []
lastCheese = 0
meltingTime = 0


visit[0][0] = True
q.append([0, 0])
while True:
    while len(q) != 0:
        n = q.pop(0)
        for d in delta:
            dx = n[0] + d[0]
            dy = n[1] + d[1]

            if (0 <= dx < R) and (0 <= dy < C) and not visit[dx][dy]:
                visit[dx][dy] = True
                if pan[dx][dy] == 0:
                    q.append([dx, dy])
                else:
                    melt.append([dx, dy])

    if len(melt) != 0:
        lastCheese = len(melt)

        for _ in range(lastCheese):
            n = melt.pop(0)
            pan[n[0]][n[1]] = 0
            q.append(n)

        meltingTime += 1
    else:
        break


print(meltingTime)
print(lastCheese)


# 치즈가 아니라 공기를 탐색
# 녹은 치즈 부분을 다시 큐에 넣는 꼼수 사용
# 한번 방문한 곳은 다시 방문하지 않는 방식으로
