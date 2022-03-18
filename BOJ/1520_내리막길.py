import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

n, m = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(m)] for _ in range(n)]
dp[n-1][m-1] = 1
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
cnt = 0


def dfs(x, y):
    if (x == n - 1 and y == m - 1) or dp[x][y] > -1:
        return dp[x][y]

    dp[x][y] = 0

    for d in delta:
        dx = d[0] + x
        dy = d[1] + y

        if 0 <= dx < n and 0 <= dy < m:
            if MAP[x][y] > MAP[dx][dy]:
                dp[x][y] += dfs(dx, dy)

    return dp[x][y]


print(dfs(0, 0))

"""
dp와 dfs를 같이 사용한 문제

dp의
-1 : 가지 않은 길
0 이상 : 방문한 길
로 설정하였다.

dp로 길의 갯수를 세야하고 방문처리를 동시에 해야하기 때문에
0으로 초기화를 하면 안된다.
반례) 도착지에 도달하지 못한 경로를 다시 가면 안되는데, 0으로 초기화를 하게 되면
그대로 그 길을 다시 가게 될수도 있다.

따라서 가면 안되는 길을 표시해주어야 한다. (방문처리를 해주어야한다)
dp의 숫자 자체가 경로의 개수를 나타내기 때문에 위처럼 구분하지 않으면 안된다.
(초기화를 0으로 할 경우 가면 안되는 길과 방문처리의 구분이 되지 않는다.)
"""