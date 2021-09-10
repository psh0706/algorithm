import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
Edge = []
head = [0 for _ in range(N+1)]


def make():
    for i in range(N+1):
        if i == 0:
            continue
        head[i] = i


def find(a):
    if head[a] == a:
        return head[a]
    head[a] = find(head[a])
    return head[a]


def union(a, b):
    aHead = find(a)
    bHead = find(b)

    if aHead == bHead:
        return False

    head[bHead] = aHead
    return True


for _ in range(M):
    start, end, weight = map(int, sys.stdin.readline().split())
    Edge.append([weight, start, end])
Edge.sort(key=lambda x: x[0])

make()
acc = 0
for e in Edge:

    if union(e[1], e[2]):
        acc += e[0]

print(acc)