n = int(input())
arr = {i: [] for i in range(1, n + 1)}
visit = []
maxDepth = 0
maxNode = 0


def setVisit():
    global visit
    visit = [False for _ in range(n+1)]


def setMaxDepth():
    global maxDepth
    maxDepth = 0


def dfs(depth, node):
    isLeaf = True

    for [nextNode, value] in arr[node]:
        if not visit[nextNode]:
            visit[nextNode] = True
            dfs(depth+value, nextNode)
            isLeaf = False

    if isLeaf:
        global maxDepth, maxNode
        if maxDepth < depth:
            maxDepth = depth
            maxNode = node
    return


def solution():
    for _ in range(n):
        info = list(map(int, input().split()))
        s = info[0]
        for i in range(1, len(info), 2):
            if info[i] == -1:
                break
            arr[s].append([info[i], info[i+1]])

    setVisit()
    visit[1] = True
    dfs(0, 1)

    setVisit()
    setMaxDepth()
    visit[maxNode] = True
    dfs(0, maxNode)

    print(maxDepth)


solution()

"""
트리의 지름 구하기
1. 어떤 임의의 노드 x 에서 가장 먼 노드 a를 구한다.
2. 노드 a 에서 부터 가장 먼 노드 b 를 구한다.
3. 노드 a와 b 사이의 거리가 트리의 지름
"""