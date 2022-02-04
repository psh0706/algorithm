from collections import deque


def solution():
    C, R = map(int, input().split())
    visit = [[False for _ in range(C)] for _ in range(R)]
    delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    ripes = deque()
    unripe = 0
    box = []
    for i in range(R):
        line = list(map(int, input().split()))
        for j in range(C):
            if line[j] == -1 or line[j] == 1:
                if line[j] == 1:
                    ripes.append([i, j])
                visit[i][j] = True
            else:
                unripe += 1

        box.append(line)

    cnt = 0
    while ripes:
        size = len(ripes)
        cnt += 1
        for _ in range(size):
            tomato = ripes.popleft()
            for d in delta:
                dx = tomato[0] + d[0]
                dy = tomato[1] + d[1]
                if 0 <= dx < R and 0 <= dy < C and not visit[dx][dy]:
                    visit[dx][dy] = True
                    ripes.append([dx, dy])
                    unripe -= 1

    if unripe == 0:
        print(cnt - 1)
    else:
        print(-1)


solution()

"""
익은토마토를 먼저 선별해서 방문처리 + 큐에 미리 삽입
아무것도 없는 칸 (== 벽) 역시 미리 파악해서 방문처리.
bfs step == 1일 이므로 스텝별로 bfs 진행.

+) 다 좋았는데 일반 list 사용시 시간초과. deque() 사용으로 해결
   box 의 크기가 1000 * 1000 이므로 시간초과 유의 
"""
