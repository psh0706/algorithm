import sys
sys.setrecursionlimit(10**4)

edge = []
tempCosts = []
visit = []
dfsMax = [0, 0]


def dfs(root, cnt):
    global dfsMax
    if dfsMax[0] < cnt:
        dfsMax = [cnt, root]

    for v in edge[root]:
        if not visit[v[0]]:
            visit[v[0]] = True
            dfs(v[0], cnt + v[1])
            visit[v[0]] = False


def solution():
    global tempCosts, edge, visit
    n = int(input())
    visit = [False for _ in range(n+1)]
    edge = [[] for _ in range(n+1)]

    for _ in range(n-1):
        parent, child, cost = map(int, input().split())
        edge[parent].append([child, cost])
        edge[child].append([parent, cost])

    # 지름을 이루는 노드 중 하나 셋팅.
    edge[0] = [[1, 0]]
    dfs(0, 0)
    a = dfsMax[1]

    # 나머지 한 노드를 찾고, 최대값 출력
    edge[0] = [[a, 0]]
    dfs(0, 0)
    print(dfsMax[0])


solution()


"""
BOJ 문제를 풀 때는 재귀 뎁스를 꼼곰히 확인할것
depth 마지노선 = 998

뎁스를 늘려야 할 때는 무지성으로 늘리면 x
잘계산해서 필요한 만큼만 늘릴것.
"""