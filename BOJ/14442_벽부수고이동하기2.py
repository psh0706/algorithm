from collections import deque

n, m, k = map(int, input().split())
MAP = []
for _ in range(n):
    line = list(map(int, list(input())))
    MAP.append(line)
visit = [[[False for _ in range(m)] for _ in range(n)] for _ in range(k+1)]
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]


class Node:
    def __init__(self, x, y, smash, step):
        self.x = x
        self.y = y
        self.smash = smash
        self.step = step


q = deque([Node(0, 0, k, 1)])
visit[k][0][0] = True
answer = -1

while q:
    node = q.popleft()

    for d in delta:

        dx = d[0] + node.x
        dy = d[1] + node.y

        if dx == n - 1 and dy == m - 1:
            answer = node.step + 1
            break

        if 0 <= dx < n and 0 <= dy < m :
            if MAP[dx][dy] == 1:
                if node.smash > 0 and not visit[node.smash - 1][dx][dy]:
                    # 벽 뚫기
                    q.append(Node(dx, dy, node.smash - 1, node.step + 1))
                    visit[node.smash - 1][dx][dy] = True
                else:
                    # 벽 못 뚫는 경우
                    continue
            else:
                if not visit[node.smash][dx][dy]:
                    # 그냥 길
                    q.append(Node(dx, dy, node.smash, node.step + 1))
                    visit[node.smash][dx][dy] = True
                else:
                    # 길 못 가는 경우 = 방문처리 된 경우
                    continue

print(answer)

"""
<1차시도>
1. bfs, node = [x, y, smash]
2. 방문처리는 K+1개의 맵으로
3. 만약 가야하는 곳이 벽인데 k=0: 소멸 
   만약 가야하는 곳이 벽인데 K > 0 : smash -= 1 and 큐 삽입.

→ 한번에 AC n, m 을 확인하는 부분을 수정하면 좀 더 빠를 것으로 예상된다.
"""