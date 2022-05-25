n = int(input())
m = int(input())
info = {i: [] for i in range(1, n+1)}
for _ in range(m):
    s, e = map(int, input().split())
    info[s].append(e)
    info[e].append(s)

visit = [False for _ in range(n+1)]
q = [1]
visit[1] = True
cnt = 0

while q:
    node = q.pop()

    for nxt in info[node]:
        if visit[nxt]:
            continue
        else:
            visit[nxt] = True
            q.append(nxt)
            cnt += 1

print(cnt)

"""
간단한 bfs 문제
"""