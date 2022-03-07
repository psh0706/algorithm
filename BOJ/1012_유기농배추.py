delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
T = int(input())

for _ in range(T):
    m, n, k = map(int, input().split())
    MAP = [[0 for _ in range(n)] for _ in range(m)]
    cabbages = []
    for _ in range(k):
        x, y = map(int, input().split())
        MAP[x][y] = 1
        cabbages.append([x, y])

    visit = [[False for _ in range(n)] for _ in range(m)]
    cnt = 0

    for [x, y] in cabbages:
        if visit[x][y]:
            continue

        q = [[x, y]]
        visit[x][y] = True
        while q:
            [cX, cY] = q.pop(0)

            for d in delta:
                dx = cX + d[0]
                dy = cY + d[1]

                if 0 <= dx < m and 0 <= dy < n and not visit[dx][dy]:
                    if MAP[dx][dy] == 1:
                        visit[dx][dy] = True
                        q.append([dx, dy])

        cnt += 1

    print(cnt)


"""
4963번 섬의개수 문제와 거의 동일한 문제로, 배추의 위치에서부터 bfs해나가며 배추 군락(덩어리)의 개수를 찾아내면 되는 문제이다.
다른점은 섬의개수 문제의 경우 2중 for문을 이용해 전체탐색을 하며 지형을 파악했으나
본 문제에서는 지형(여기서는 배추) 의 리스트를 미리 받아서 진행했다는 점이다 -> 시간복잡도가 더 적은 문제이다.
리스트를 미리 받아서 진행하는것은 섬의개수 류의 문제에서 동일하게 사용할 수 있는 스킬같다.
"""