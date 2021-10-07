N, M, K = map(int, input().split())
Edge = []
head = [0]*(N+1)
for i in range(1, M+1):
    start, end = map(int, input().split())
    Edge.append([start, end, i])


def make():
    for h in range(N+1):
        head[h] = h


def find(a):
    if head[a] == a:
        return head[a]
    head[a] = find(head[a])
    return head[a]


def union(a, b):
    aHead = find(a)
    bHead = find(b)

    if aHead == bHead:
        # 사이클이 형성된 것임
        return False

    # 정점 b와 a를 연결
    head[bHead] = aHead
    return True


result = ""
for _ in range(K):
    acc = 0
    mCnt = 0
    make()
    temp = []
    for e in Edge:
        if union(e[0], e[1]):
            temp.append(e)
            acc += e[2]
            mCnt += 1

    if mCnt == N-1:
        result += str(acc) + ' '
    else:
        result += '0 '
    Edge.pop(0)

print(result)

"""
간선을 중심으로 진행되는 MST 문제.
한 턴마다 가장 작은 간선을 삭제해야하는데 프림보다는 크루스칼이 구현하기 좋겠다고 판단.
MST 에서 간선의 갯수는 N-1 이라는것을 꼭 명심해야한다.
"""