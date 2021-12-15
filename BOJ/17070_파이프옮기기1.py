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
상태 3개를 다른 dp 테이블로 나누어서 계산한다.
(n,n) 칸에 도달할 때 까지 테이블들을 순회하고, 계산이 끝나면 세 상태를 모두 더해준다.
"""

"""
틀렸습니다 1회 -> 대각선 확인 시 
MAP[i + 1][j] == 0 and MAP[i][j + 1] == 0 and MAP[i][j] (x)
MAP[i + 1][j] == 0 and MAP[i][j + 1] == 0 and MAP[i+1][j+1] (0) 
수정 후 AC
"""