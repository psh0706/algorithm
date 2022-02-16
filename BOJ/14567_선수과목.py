from copy import deepcopy

n, m = map(int, input().split())
semesters = [0 for _ in range(n+1)]
inDegree = [0 for _ in range(n+1)]
info = [[] for _ in range(n+1)]
for _ in range(m):
    pre, pro = map(int, input().split())
    info[pre].append(pro)
    inDegree[pro] += 1

q = []

for i in range(1, n+1):
    if inDegree[i] == 0:
        q.append(i)
        semesters[i] = 1


while q:
    node = q.pop(0)
    for n in info[node]:
        inDegree[n] -= 1
        if inDegree[n] == 0:
            q.append(n)
            semesters[n] = semesters[node] + 1

print(' '.join(map(str, semesters[1:])))


"""
단순 구현으로 접근 했으나, 위상정렬 문제였다.
indegree 개념을 이용하여, 나에게 들어오는 그래프(간선)이 없을 시 수행하는 것을 반복하면 된다.
"""