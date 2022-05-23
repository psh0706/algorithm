r, c = map(int, input().split())
cctvList = []
moveList = []
MAP = []
move = {
    1: [[[0, 1]], [[0, -1]], [[1, 0]], [[-1, 0]]],
    2: [[[0, 1], [0, -1]], [[1, 0], [-1, 0]]],
    3: [[[0, 1], [-1, 0]], [[-1, 0], [0, -1]], [[0, -1], [1, 0]], [[1, 0], [0, 1]]],
    4: [[[0, 1], [-1, 0], [0, -1]], [[-1, 0], [0, -1], [1, 0]], [[0, -1], [1, 0], [0, 1]], [[1, 0], [0, 1], [-1, 0]]],
    5: [[[0, 1], [0, -1], [1, 0], [-1, 0]]]
}


def dfs(depth, string):
    if depth == len(cctvList):
        moveList.append(list(map(int, list(string))))
        return

    [x, y] = cctvList[depth]
    for i in range(len(move[MAP[x][y]])):
        dfs(depth+1, string+str(i))


def solution():
    B_SPOT = r * c

    for i in range(r):
        line = list(map(int, input().split()))
        for j in range(c):
            if line[j] == 6:
                B_SPOT -= 1
            elif 1 <= line[j] <= 5:
                B_SPOT -= 1
                cctvList.append([i, j])
        MAP.append(line)

    dfs(0, "")
    answer = B_SPOT

    for i in range(len(moveList)):
        visit = [[False for _ in range(c)] for _ in range(r)]
        n = B_SPOT
        for j in range(len(moveList[i])):
            [x, y] = cctvList[j]
            visit[x][y] = True
            moveIdx = moveList[i][j]
            delta = move[MAP[x][y]][moveIdx]
            for d in delta:
                dx = x
                dy = y
                while True:
                    dx += d[0]
                    dy += d[1]
                    if 0 <= dx < r and 0 <= dy < c and MAP[dx][dy] != 6:
                        if not visit[dx][dy] and MAP[dx][dy] == 0:
                            n -= 1
                            visit[dx][dy] = True
                    else:
                        break

        answer = min(n, answer)

    print(answer)


solution()


"""
dfs 를 이용해 cctv 들이 바라볼 수 있는 case 를 모두 구하고
각 case 별 사각지대 수를 구한 뒤 그 중 최소값을 고른다.
"""