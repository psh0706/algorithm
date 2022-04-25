def solution():
    n = int(input())
    MAP = [list(map(int, input().split(' '))) for _ in range(n)]
    island = {}
    delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    visit = [[False for _ in range(n)] for _ in range(n)]
    islandNum = 1

    # 섬 파악
    for i in range(n):
        for j in range(n):
            if visit[i][j] or MAP[i][j] == 0:
                continue

            q = [[i, j]]
            visit[i][j] = True
            temp = []

            while q:
                flag = True
                node = q.pop(0)
                MAP[node[0]][node[1]] = islandNum

                for d in delta:
                    dx = node[0] + d[0]
                    dy = node[1] + d[1]

                    if 0 <= dx < n and 0 <= dy < n and not visit[dx][dy]:
                        if MAP[dx][dy] == 1:
                            visit[dx][dy] = True
                            q.append([dx, dy])
                        else:
                            if flag:
                                flag = False
                                temp.append(node)

            island[islandNum] = temp
            islandNum += 1

    # 섬 외곽으로 BFS -> 최소값을 찾는다.
    MIN = 999
    for key in island:
        visit = [[False for _ in range(n)] for _ in range(n)]
        cnt = 0
        q = island[key]
        for [x, y] in q:
            visit[x][y] = True

        while q:
            quitFlag = False
            size = len(q)
            cnt += 1
            for _ in range(size):
                node = q.pop(0)

                for d in delta:
                    dx = d[0] + node[0]
                    dy = d[1] + node[1]

                    if 0 <= dx < n and 0 <= dy < n and not visit[dx][dy]:
                        if MAP[dx][dy] != 0 and MAP[dx][dy] != key:
                            MIN = min(MIN, cnt-1)
                            quitFlag = True
                            break

                        elif MAP[dx][dy] == 0:
                            visit[dx][dy] = True
                            q.append([dx, dy])

                if quitFlag:
                    break

    print(MIN)


solution()

"""
1. 섬을 파악하며 각 섬 별로 MAP 에 넘버링을 하고, 섬 외곽 (=섬이 아닌 곳과 맞닿아 있는 부분)을 따로 저장한다.
2. 섬 외곽으로 bfs 하며 다른 섬에 닿을 때 까지의 거리를 count 한다. 그 값중 최소값을 찾는다.
"""