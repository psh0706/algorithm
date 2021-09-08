import sys
from collections import deque
from copy import deepcopy

N, M, D = map(int, sys.stdin.readline().split())
MAP = deque()
enemy = 0
ArcherList = deque()
allCase = []
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for _ in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    MAP.append(temp)
    enemy += sum(temp)


def combination(depth, start, result):
    if depth == 3:
        ArcherList.append(list(map(int, result.split())))
        return

    for i in range(start, M):
        combination(depth + 1, i + 1, result + str(i) + " ")


combination(0, 0, "")

for Archer in ArcherList:
    copyMAP = deepcopy(MAP)
    takeCnt = 0
    disappoint = 0

    while enemy != disappoint:
        take = []
        for A in Archer:
            q = deque([[N, A]])
            visit = [[False for _ in range(M)] for _ in range(N)]
            local = []
            cnt = 0

            while cnt != D:
                size = len(q)
                for _ in range(size):

                    n = q.popleft()

                    for d in delta:
                        dx = n[0] + d[0]
                        dy = n[1] + d[1]

                        if 0 <= dx < N and 0 <= dy < M and not visit[dx][dy]:
                            if copyMAP[dx][dy] == 1:
                                local.append([dx, dy])
                            else:
                                visit[dx][dy] = True
                                q.append([dx, dy])
                cnt += 1

                if local:
                    local.sort(key=lambda x: x[1])
                    take.append(local[0])
                    break

        for t in take:
            if copyMAP[t[0]][t[1]] == 1:
                takeCnt += 1
                disappoint += 1
                copyMAP[t[0]][t[1]] = 0
            else:
                continue

        end = copyMAP.pop()
        disappoint += sum(end)
        copyMAP.appendleft([0 for _ in range(M)])

    allCase.append(takeCnt)

print(max(allCase))


# 빡구현 문제 캐슬디펜스!
# mutable 한 객체는 단순 대입으로는 얕은 복사밖에 일어나지 않는다 (두 변수가 같은 메모리를 바라보기 떄문).
# 그 사실을 모르고 30 번 line 을 단순 대입 처리 했다가 MAP 자체가 변해버려서 버그가 생겼었다
# 1차원 mutable 객체 같은 경우 슬라이싱 [:] 을 이용하면 깊은 복사가 되지만
# 2차원 mutable 객체 같은 경우 mutable 객체 안의 mutable 객체 이기 때문에 슬라이싱을 이용해도 내부의 객체들은 같은 주소를 바라본다.
# 내부 객체들까지 모두 깊은 복사를 하려면 copy.deepcopy 메소드를 이용해야했다.
# 메모리주소.. 포인터 관리의 중요성 ㅎㅎ
# 원샷 원킬해서 기분좋음

