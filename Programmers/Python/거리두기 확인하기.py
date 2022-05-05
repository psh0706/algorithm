def bfs(MAP):
    n, m = len(MAP), len(MAP[0])
    delta = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    pList = []

    for i in range(n):
        for j in range(m):
            if MAP[i][j] == 'P':
                pList.append([i, j])

    for p in pList:
        q = [[p[0], p[1], 0]]
        visit = [[False for _ in range(m)] for _ in range(n)]
        visit[p[0]][p[1]] = True

        while q:
            node = q.pop(0)

            for d in delta:
                dx = node[0] + d[0]
                dy = node[1] + d[1]
                if 0 <= dx < n and 0 <= dy < m and not visit[dx][dy]:
                    if MAP[dx][dy] == 'P':
                        if node[2]+1 <= 2:
                            return 0
                    elif MAP[dx][dy] == 'O':
                        visit[dx][dy] = True
                        q.append([dx, dy, node[2] + 1])

    return 1


def solution(places):
    answer = []

    for place in places:
        answer.append(bfs(place))

    return answer


solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])