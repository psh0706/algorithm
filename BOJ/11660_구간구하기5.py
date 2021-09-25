import sys

N, M = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
sections = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
result = ""

dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        dp[i + 1][j + 1] = dp[i + 1][j] + dp[i][j + 1] - dp[i][j] + MAP[i][j]

for section in sections:
    x1, y1, x2, y2 = section[0], section[1], section[2], section[3]
    result += str(dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]) + "\n"

print(result)

"""for section in sections:
    x1 = section[0] - 1
    y1 = section[1] - 1
    x2 = section[2] - 1
    y2 = section[3] - 1
    acc = 0

    visit = [[False for _ in range(N)] for _ in range(N)]
    visit[x1][y1] = True
    acc += MAP[x1][y1]
    q = deque([[x1, y1]])

    while q:
        n = q.popleft()

        for d in delta:
            dx = n[0] + d[0]
            dy = n[1] + d[1]

            if 0 <= dx < N and 0 <= dy < N and not visit[dx][dy]:
                if x1 <= dx <= x2 and y1 <= dy <= y2 and not visit[dx][dy]:
                    acc += MAP[dx][dy]
                visit[dx][dy] = True
                q.append([dx, dy])

    print(acc)"""


"""
첫 dp 문제..
머야 쉽네~ 하고 호기롭게 BFS 로 접근했다가 시간초과로 몇 방 먹었다 ㅠㅠ
결국 검색을 통해 dp 문제라는걸 깨닫고 다시 풀어보았다.
dp로 미리 부분합 테이블을 만들어 둔 뒤 
x2 y2 까지의 부분합 에서 필요없는 부분합을 빼고(x1 - 1, y2) (x2, y1 - 1) 두번 뺀 부분은 다시 한번 더해서 (x1 - 1)(y1 - 1) 
원하는 부분의 부분합을 구하는 문제
dp 테이블을 1칸씩 늘리는것이 포인트였다.
"""
