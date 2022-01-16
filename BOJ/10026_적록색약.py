class Node:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color


def bfs(n, MAP):
    area = 0
    delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    visit = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visit[i][j]:
                continue

            visit[i][j] = True
            q = [Node(i, j, MAP[i][j])]

            while q:
                node = q.pop()
                for d in delta:
                    dx = node.x + d[0]
                    dy = node.y + d[1]

                    if 0 <= dx < n and 0 <= dy < n and not visit[dx][dy]:
                        if MAP[dx][dy] == node.color:
                            q.append(Node(dx, dy, node.color))
                            visit[dx][dy] = True

            area += 1

    return area


def solution():
    n = int(input())
    grid = []
    weekGrid = []

    for _ in range(n):
        line = input()
        grid.append(list(line))
        weekGrid.append(list(line.replace('G', 'R')))

    print(bfs(n, grid), bfs(n, weekGrid))


solution()


"""
일반 그리드, 색약용 그리드를 만들어주고
각자를 bfs 했다.
"""