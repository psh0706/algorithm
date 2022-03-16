import copy


def rotate90(shape):
    result = []
    baseLine = shape
    for _ in range(3):
        temp = []
        for i in range(4):
            temp.append([-1 * baseLine[i][1], baseLine[i][0]])
        result.append(temp)
        baseLine = copy.deepcopy(temp)
    return result


def solution():
    n, m = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(n)]
    tetromino = [[[0, 0], [0, 1], [0, 2], [0, 3]],
                 [[0, 0], [0, 1], [1, 0], [1, 1]],
                 [[0, 0], [0, 1], [0, 2], [1, 1]],
                 [[0, 0], [1, 0], [2, 0], [2, 1]],
                 [[0, 0], [1, 0], [2, 0], [2, -1]],
                 [[0, 0], [1, 0], [1, 1], [2, 1]],
                 [[0, 0], [1, 0], [1, -1], [2, -1]]]

    for i in range(len(tetromino)):
        tetromino += rotate90(tetromino[i])

    MAX = 0
    for i in range(n):
        for j in range(m):
            for t in tetromino:
                cnt = 0
                flag = False
                for d in t:
                    dx = i + d[0]
                    dy = j + d[1]

                    if 0 <= dx < n and 0 <= dy < m:
                        cnt += MAP[dx][dy]
                    else:
                        flag = True
                        break
                if flag:
                    continue
                else:
                    MAX = max(cnt, MAX)
    print(MAX)


solution()
