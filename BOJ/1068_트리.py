def checkLeaf(n, info):
    isChild = [False for _ in range(n)]
    for i in range(n):
        if info[i] == -1:
            continue
        else:
            isChild[info[i]] = True
    return isChild


def solution():
    n = int(input())
    info = list(map(int, input().split()))
    delNode = int(input())
    isChild = checkLeaf(n, info)
    visit = [False for _ in range(n)]

    # delete node
    q = [delNode]
    visit[delNode] = True

    while q:
        node = q.pop(0)
        for i in range(len(info)):
            if info[i] == node:
                if isChild[i]:
                    q.append(i)
                    visit[i] = True
                else:
                    visit[i] = True

    # check leaf node
    isLeaf = [True for _ in range(n)]
    for i in range(n):
        if visit[i]:
            isLeaf[i] = False
        elif info[i] == -1:
            continue
        else:
            isLeaf[info[i]] = False
    print(isLeaf.count(True))


solution()

"""
1. 자식 노드 여부를 체크한다. (=isChild)
2. 지울 노드부터 시작해서 그것의 자식 노드들을 방문해 나간다.
    방문한 노드가 자식이 있는 노드이다 -> 큐에 해당 노드를 넣고 방문처리한다.
    자식이 없는 노드이다. -> 방문처리만 한다.
3. 방문 정보를 토대로 다시 리프노드를 판단한다.
    -> 방문 한 노드는 지울 노드를 의미하므로, 별도의 작업 없이 False 로 바꾸어 준다.
    -> 방문하지는 않았지만, 부모 노드가 없다면 판단의미가 없으므로 넘어간다.
    -> 방문하지 않았고 부모노드가 있는 노드는 리프노드 판단 대상이므로, 해당 노드의 부모 노드를 False 로 바꾸어준다.
       (부모 노드 이기만 하면, 리프노드가 아니라는 의미이다.)
4. 위 과정을 모두 거친 후 리프노드만을 count 한다.
"""