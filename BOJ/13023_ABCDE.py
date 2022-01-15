n, m = map(int, input().split())
edge = dict.fromkeys(range(n))

for _ in range(m):
    start, end = map(int, input().split())
    if edge[start]:
        edge[start].append(end)
    else:
        edge[start] = [end]

    if edge[end]:
        edge[end].append(start)
    else:
        edge[end] = [start]


visit = [False for _ in range(n)]
flag = 0


def recursion(depth, st):
    global flag

    if depth == 5:
        flag = 1
        return

    if edge[st] is None:
        return

    for ed in edge[st]:
        if visit[ed]:
            continue

        visit[ed] = True
        recursion(depth+1, ed)

        if flag:
            return

        visit[ed] = False


for i in range(n):
    if flag:
        break

    visit[i] = True
    recursion(1, i)
    visit[i] = False

print(flag)

