import sys

R, C = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
visit = [[0 for _ in range(C)] for _ in range(R)]
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
q = []
melt = []
lastCheese = 0
meltingTime = 0


visit[0][0] += 1
q.append([0, 0])
while True:
    while len(q) != 0:
        n = q.pop(0)
        for d in delta:
            dx = n[0] + d[0]
            dy = n[1] + d[1]

            if (0 <= dx < R) and (0 <= dy < C):
                if MAP[dx][dy] == 0 and visit[dx][dy] >= 1:
                    continue

                visit[dx][dy] += 1
                if MAP[dx][dy] == 0:
                    q.append([dx, dy])
                elif MAP[dx][dy] == 1 and visit[dx][dy] == 2:
                    melt.append([dx, dy])

    if melt:
        lastCheese = len(melt)

        for _ in range(lastCheese):
            n = melt.pop(0)
            MAP[n[0]][n[1]] = 0
            q.append(n)

        meltingTime += 1
    else:
        break


print(meltingTime)


"""
골드 5 치즈 문제랑 같은듯 다른 문제
공기중에 표면이 2면 이상 드러난 곳만 녹는다는것이 다른점이다.
똑같이 공기를 BFS로 탐색하는데 방문처리를 True, False 가 아니라 counting 하는 방식으로 해결했다.
"""
