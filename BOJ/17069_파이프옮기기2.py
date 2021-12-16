n = int(input())
MAP = [list(map(int, input().split())) for _ in range(n)]
width = [[0 for _ in range(n)] for _ in range(n)]
vertical = [[0 for _ in range(n)] for _ in range(n)]
diagonal = [[0 for _ in range(n)] for _ in range(n)]

width[0][1] = 1

for i in range(n):
    for j in range(n):

        if width[i][j] > 0:
            if j+1 < n and MAP[i][j+1] == 0:
                width[i][j+1] += width[i][j]
            if i+1 < n and j+1 < n and MAP[i+1][j] == 0 and MAP[i][j+1] == 0 and MAP[i+1][j+1] == 0:
                diagonal[i+1][j+1] += width[i][j]

        if vertical[i][j] > 0:
            if i + 1 < n and MAP[i + 1][j] == 0:
                vertical[i+1][j] += vertical[i][j]
            if i + 1 < n and j + 1 < n and MAP[i + 1][j] == 0 and MAP[i][j + 1] == 0 and MAP[i+1][j+1] == 0:
                diagonal[i + 1][j + 1] += vertical[i][j]

        if diagonal[i][j] > 0:
            if j + 1 < n and MAP[i][j + 1] == 0:
                width[i][j + 1] += diagonal[i][j]
            if i + 1 < n and MAP[i + 1][j] == 0:
                vertical[i + 1][j] += diagonal[i][j]
            if i + 1 < n and j + 1 < n and MAP[i + 1][j] == 0 and MAP[i][j + 1] == 0 and MAP[i+1][j+1] == 0:
                diagonal[i + 1][j + 1] += diagonal[i][j]

print(diagonal[n-1][n-1] + vertical[n-1][n-1] + width[n-1][n-1])

"""
파이프옮기기 1번과 같은 문제
1번을 dfs 나 bfs 로 푼 사람들이 dp로 풀 수 있도록 n의 범위가 좀 더 크다.
"""