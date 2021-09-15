import sys
from copy import deepcopy


def check():
    checkVisit = [[False for _ in range(M)] for _ in range(N)]
    clone = deepcopy(MAP)
    global maxi
    safeArea = area - 3

    for virus in virusIndex:
        q = [virus]
        checkVisit[virus[0]][virus[1]] = True

        while len(q) != 0:
            n = q.pop(0)

            for d in delta:
                dx = n[0] + d[0]
                dy = n[1] + d[1]

                if 0 <= dx < N and 0 <= dy < M and not checkVisit[dx][dy]:
                    if clone[dx][dy] == 0:
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
        # for m in MAP:
        #     print(m)
        # print('-----------')
        return

    while x != N and y != M:
        if MAP[x][y] == 0:
            MAP[x][y] = 1
            recursion(depth + 1, x, y+1)
            MAP[x][y] = 0
        y += 1
        if y == M:
            x += 1
            y -= y



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
    answerList = []
    maxi = 0

    recursion(0, 0, 0)
    print(maxi)
