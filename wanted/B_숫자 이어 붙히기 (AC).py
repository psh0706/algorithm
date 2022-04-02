N, Q = map(int, input().split())
number = list(map(int, input().split()))
edge = {i: [] for i in range(N)}
play = []

for _ in range(N-1):
    a, b = map(int, input().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)

for _ in range(Q):
    to, go = map(int, input().split())
    play.append([to - 1, go - 1])

for p in play:
    to, go = p[0], p[1]
    q = [[to, str(number[to])]]
    visit = [False for _ in range(N+1)]
    visit[to] = True

    while q:
        node = q.pop(0)

        if node[0] == go:
            print(node[1])
            break

        for i in edge[node[0]]:
            if not visit[i]:
                visit[i] = True
                string = str(node[1]) + str(number[i])
                temp = int(string) % 1000000007
                q.append([i, str(temp)])

