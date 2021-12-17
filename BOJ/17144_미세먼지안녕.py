R, C, T = map(int, input().split())
MAP = []
cleaner = []
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for x in range(R):
    line = list(map(int, input().split()))
    if line[0] == -1:
        line[0] = 0
        cleaner.append(x)
    MAP.append(line)

for t in range(T):
    # 먼지 확인 & 확산
    tempMAP = [[0 for _ in range(C)] for _ in range(R)]
    for x in range(R):
        for y in range(C):
            # 먼지 개수가 5개 이상인 것만 확산 될 수 있다.
            if MAP[x][y] >= 5:
                particle = int(MAP[x][y] / 5)
                cnt = 0
                for d in delta:
                    dx = d[0] + x
                    dy = d[1] + y

                    # 범위 안에 있고, 공청기가 아닌지 확인
                    if 0 <= dx < R and 0 <= dy < C:
                        if not (dx == cleaner[0] and dy == 0) and not (dx == cleaner[1] and dy == 0):
                            tempMAP[dx][dy] += particle
                            cnt += particle
                tempMAP[x][y] += (MAP[x][y] - cnt)
            elif MAP[x][y] > 0:
                tempMAP[x][y] += MAP[x][y]
    MAP = tempMAP

    # 공기 청정기 작동
    # 순환 1
    # ->
    up1 = MAP[cleaner[0]].pop(-1)
    MAP[cleaner[0]].insert(0, 0)
    # ^
    left1 = MAP[0][-1]
    for i in range(1, cleaner[0]):
        MAP[i-1][-1] = MAP[i][-1]
    MAP[cleaner[0]-1][-1] = up1
    # <-
    MAP[0].insert(C-1, left1)
    down1 = MAP[0].pop(0)
    # v
    for i in range(cleaner[0], 0, -1):
        MAP[i+1][0] = MAP[i][0]
    MAP[1][0] = down1
    MAP[cleaner[0]][0] = 0

    # 순환 2
    # ->
    down2 = MAP[cleaner[1]].pop(-1)
    MAP[cleaner[1]].insert(0, 0)
    # v
    left2 = MAP[R-1][-1]
    for i in range(R-2, cleaner[1], -1):
        MAP[i+1][-1] = MAP[i][-1]
    MAP[cleaner[1]+1][-1] = down2
    # <-
    MAP[R-1].insert(C-1, left2)
    up2 = MAP[R-1].pop(0)
    # ^
    for i in range(cleaner[1]+1, R-1):
        MAP[i-1][0] = MAP[i][0]
    MAP[R-2][0] = up2
    MAP[cleaner[1]][0] = 0

print(sum(list(map(sum, MAP))))

"""
빡구현 문제
49번 line 의 for 문의 방향이 잘못되어서 틀렸습니다 폭탄을 맞았다 ㅠㅠ
설계와 테케의 중요성...ㅠㅠㅠㅠ
"""