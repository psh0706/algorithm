N = int(input())
price = list(map(int, input().split()))
discount = []
for _ in range(N):
    n = int(input())
    temp = [list(map(int, input().split())) for _ in range(n)]
    discount.append(temp)
MIN = 9999999
visit = [False for _ in range(N)]


def dfs(depth, cnt):
    if depth == N:
        global MIN
        MIN = min(MIN, cnt)
        return

    for i in range(N):
        if visit[i]:
            continue

        if price[i] < 1:
            cnt += 1
        else:
            cnt += price[i]
        visit[i] = True
        disInfo = discount[i]
        for dis in disInfo:
            price[dis[0]-1] -= dis[1]

        dfs(depth+1, cnt)

        visit[i] = False
        if price[i] < 1:
            cnt -= 1
        else:
            cnt -= price[i]
        for dis in disInfo:
            price[dis[0]-1] += dis[1]


dfs(0, 0)
print(MIN)
