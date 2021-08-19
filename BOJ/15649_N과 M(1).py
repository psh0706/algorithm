import sys

n, m = map(int, sys.stdin.readline().split(' '))
arr = []
visit = list([False for i in range(n)])


def permission(depth):
    if depth == m:
        print(" ".join(str(i) for i in arr))
        return

    for i in range(0, n):
        if visit[i]: continue
        visit[i] = True
        arr.append(i + 1)
        permission(depth + 1)
        visit[i] = False
        arr.pop()


permission(0)
