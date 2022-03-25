def checkBomb(MAP, R, C):
    empty = []
    bomb = []
    for i in range(R):
        for j in range(C):
            if MAP[i][j] == ".":
                empty.append([i, j])
            else:
                bomb.append([i, j])
    return empty, bomb


def solution():
    R, C, N = map(int, input().split())
    delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    MAP = [list(input()) for _ in range(R)]
    empty, bomb = checkBomb(MAP, R, C)

    if N == 1:
        for m in MAP:
            print(''.join(m))
        return

    count = 2
    while True:
        if count % 2 == 0:
            for [x, y] in empty:
                MAP[x][y] = 'O'
        else:
            for [x, y] in bomb:
                if MAP[x][y] != '.':
                    MAP[x][y] = '.'

                for d in delta:
                    dx = x + d[0]
                    dy = y + d[1]

                    if 0 <= dx < R and 0 <= dy < C and MAP[dx][dy] != ".":
                        MAP[dx][dy] = '.'
            empty, bomb = checkBomb(MAP, R, C)

        if count == N or N == 1:
            for m in MAP:
                print(''.join(m))
            return

        count += 1


solution()

"""
간단한 구현 문제 봄버맨.
"""
