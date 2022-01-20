sudoku = []
blanks = []
blankNum = 0


def checkNum(blankX, blankY):
    visit = [False for _ in range(9)]

    # 가로
    for y in range(9):
        if sudoku[blankX][y] == 0:
            continue
        visit[sudoku[blankX][y] - 1] = True

    # 세로
    for x in range(9):
        if sudoku[x][blankY] == 0:
            continue
        visit[sudoku[x][blankY] - 1] = True

    # 구역
    idx = [[0, 3], [3, 6], [6, 9]]
    x1, x2 = 0, 0
    y1, y2 = 0, 0
    for i in range(3):
        if idx[i][0] <= blankX < idx[i][1]:
            x1 = idx[i][0]
            x2 = idx[i][1]

        if idx[i][0] <= blankY < idx[i][1]:
            y1 = idx[i][0]
            y2 = idx[i][1]

    for x in range(x1, x2):
        for y in range(y1, y2):
            if sudoku[x][y] == 0:
                continue
            visit[sudoku[x][y] - 1] = True

    left = []
    for i in range(9):
        if not visit[i]:
            left.append(i+1)

    return left


def dfs(depth):
    if depth == blankNum:
        return True

    x, y = blanks[depth][0], blanks[depth][1]
    lefts = checkNum(x, y)
    if not lefts:
        return False

    for left in lefts:
        sudoku[x][y] = left
        if dfs(depth+1):
            return True
        sudoku[x][y] = 0


def solution():
    global blankNum
    for i in range(9):
        line = list(map(int, input().split()))
        for j in range(9):
            if line[j] == 0:
                blanks.append([i, j])
        sudoku.append(line)
        blankNum = len(blanks)

    dfs(0)

    for s in sudoku:
        print(' '.join(map(str, s)))

    return


solution()


"""
dfs를 이용해 풀었다.
가로, 세로, 구역 별로 이미 적혀있는 수를 방문처리하고
남는 수를 이용해 재귀한다.
"""
