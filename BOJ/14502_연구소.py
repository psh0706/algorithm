import sys
from copy import deepcopy
from collections import deque


def check():
    checkVisit = [[False for _ in range(M)] for _ in range(N)]
    clone = deepcopy(MAP)
    global maxi
    safeArea = area - 3
    q = deque()

    for virus in virusIndex:
        q.append(virus)
        checkVisit[virus[0]][virus[1]] = True

    while len(q) != 0:
        n = q.popleft()

        for d in delta:
            dx = n[0] + d[0]
            dy = n[1] + d[1]

            if 0 <= dx < N and 0 <= dy < M and not checkVisit[dx][dy] and clone[dx][dy] == 0:
                checkVisit[dx][dy] = True
                clone[dx][dy] = 2
                safeArea -= 1
                q.append([dx, dy])

    if maxi < safeArea:
        maxi = safeArea
    return


def recursion(depth, x, y):
    if depth == 3:
        check()
        return

    while x < N:
        if 0 <= x < N and 0 <= y < M and MAP[x][y] == 0:
            MAP[x][y] = 1
            recursion(depth + 1, x, y+1)
            MAP[x][y] = 0
        if y == M:
            x += 1
            y -= y
        else:
            y += 1


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    MAP = []
    virusIndex = []
    area = 0
    for i in range(N):
        temp = list(map(int, sys.stdin.readline().split()))
        MAP.append(temp)
        for j in range(len(temp)):
            if MAP[i][j] == 0:
                area += 1
            if MAP[i][j] == 2:
                virusIndex.append([i, j])

    visit = [[False for _ in range(M)] for _ in range(N)]
    delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    maxi = 0

    recursion(0, 0, 0)

    print(maxi)

"""
재귀적으로 이차원 배열 요소들의 조합을 만들고 (모든 요소에서 3개를 선택하는 경우의 수 만들기)
벽을 3개 세울 떄 마다 (== 요소 3개 선택이 완료될 때 마다)
BFS 로 바이러스를 퍼트려 안전지대를 확인하는 로직으로 구현했다.
바이러스를 퍼트리는 것은 입력을 받을 때 미리 저장해둔 바이러스들의 위치를 이용했는데
반복문으로 바이러스들을 하나 하나 BFS 하여 퍼트리는 방식으로 구현하였다가
큐에 한번에 넣어 바이러스들을 동시에 BFS 하는 방식으로 수정했다.
안전지대를 확인하는것은 역시 입력을 받을 때 미리 카운트 해둔 안전지대의 개수를 
바이러스가 한 칸씩 퍼질 때 마다 줄여가는 것으로 반복문의 횟수를 줄였다!
설계와 구현은 어렵지 않았지만 디버깅이 조금 오래걸렸던 문제.
"""