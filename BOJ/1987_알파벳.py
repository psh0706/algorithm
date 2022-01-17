r, c = map(int, input().split())
MAP = [list(input()) for _ in range(r)]
maxi = 0
visit = [False for _ in range(26)]
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
flag = False


def dfs(depth, x, y):
    global maxi
    global flag
    maxi = max(maxi, depth)

    for d in delta:
        dx = x + d[0]
        dy = y + d[1]
        if 0 <= dx < r and 0 <= dy < c and not visit[ord(MAP[dx][dy]) - 65]:
            visit[ord(MAP[dx][dy]) - 65] = True
            dfs(depth+1, dx, dy)
            visit[ord(MAP[dx][dy]) - 65] = False


visit[ord(MAP[0][0]) - 65] = True
dfs(1, 0, 0)
print(maxi)



