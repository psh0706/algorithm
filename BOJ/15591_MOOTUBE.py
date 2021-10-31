N, Q = map(int, input().split())
INF = int(1e9)
vInfo = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b, u = map(int, input().split())
    vInfo[a-1].append([b-1, u])
    vInfo[b-1].append([a-1, u])

result = ""
for _ in range(Q):
    k, v = map(int, input().split())
    cnt = 0
    q = [v-1]
    visit = [False for _ in range(N)]
    visit[v-1] = True

    while q:
        n = q.pop()

        for e in vInfo[n]:
            if visit[e[0]]:
                continue
            if e[1] < k:
                continue

            q.append(e[0])
            cnt += 1
            visit[e[0]] = True

    result += str(cnt) + "\n"

print(result)

"""
bfs를 이용한 문제
k 값 보다 작은곳은 탐색하지 않는것이 포인트
"""