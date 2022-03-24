import heapq


class Node:
    def __init__(self, x, y, deltaX, deltaY, mirror):
        self.x = x
        self.y = y
        self.deltaX = deltaX
        self.deltaY = deltaY
        self.mirror = mirror

    def __lt__(self, other):
        return self.mirror <= other.mirror


def solution():
    delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    m, n = map(int, input().split())
    C = []
    visit = [[[int(1e9) for _ in range(4)] for _ in range(m)] for _ in range(n)]
    MAP = []
    for i in range(n):
        line = list(input())
        for j in range(m):
            if line[j] == "C":
                C.append([i, j])
        MAP.append(line)

    q = []
    heapq.heappush(q, Node(C[0][0], C[0][1], 0, 0, 0))

    while q:
        node = heapq.heappop(q)

        if node.x == C[1][0] and node.y == C[1][1]:
            print(node.mirror)
            return

        for d in range(len(delta)):
            dx = delta[d][0] + node.x
            dy = delta[d][1] + node.y

            if 0 <= dx < n and 0 <= dy < m and visit[dx][dy][d] >= node.mirror:
                if MAP[dx][dy] != '*':
                    visit[dx][dy][d] = node.mirror
                    if (node.deltaX == delta[d][0] and node.deltaY == delta[d][1]) or (node.deltaX == node.deltaY):
                        heapq.heappush(q, Node(dx, dy, delta[d][0], delta[d][1], node.mirror))
                    else:
                        heapq.heappush(q, Node(dx, dy, delta[d][0], delta[d][1], node.mirror + 1))


solution()

"""
우선순위큐를 사용한 BFS + 변형 방문처리를 사용
방문처리는 각 칸을 사방에서 접근 가능한 하나의 칸으로 보고 (칸 별로 접근할수 있는 방법 4개)
그 칸에 접근하려는 노드가 가진 거울의 개수를 비교해서 방문처리를 해주었다.
접근하려는 노드가 가진 거울의 개수가 방문처리된 거울의 개수보다 크면 더이상 그 칸을 지나가는것에 의미가 없으므로
더이상 bfs를 진행하지 않는다.
"""