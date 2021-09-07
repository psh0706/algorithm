import sys

N = int(sys.stdin.readline())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visit = [[False for _ in range(N)] for _ in range(N)]
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
q = []
fishes = []
babyShark = 2
startR, startC = 0, 0
cnt = 0
eat = 0
result = 0

for line in MAP:
    if 9 in line:
        startR = MAP.index(line)
        startC = line.index(9)
        break

MAP[startR][startC] = 0
visit[startR][startC] = True
q.append([startR, startC])

while len(q) != 0:
    size = len(q)
    for _ in range(size):
        n = q.pop(0)

        for d in delta:
            dx = n[0] + d[0]
            dy = n[1] + d[1]

            if 0 <= dx < N and 0 <= dy < N and not visit[dx][dy]:
                if 0 < MAP[dx][dy] < babyShark:
                    visit[dx][dy] = True
                    fishes.append([dx, dy])
                elif MAP[dx][dy] > babyShark:
                    continue
                else:
                    visit[dx][dy] = True
                    q.append([dx, dy])

    cnt += 1

    if len(fishes) > 0:
        X, Y = N, N
        for fish in fishes:
            if X > fish[0]:
                X = fish[0]
                Y = fish[1]
            elif X == fish[0]:
                if Y > fish[1]:
                    X = fish[0]
                    Y = fish[1]

        eat += 1
        if eat == babyShark:
            babyShark += 1
            eat = 0

        result = cnt
        fishes = []
        MAP[X][Y] = 0
        visit = [[False for _ in range(N)] for _ in range(N)]
        visit[X][Y] = True
        q = [[X, Y]]


print(result)

# 한 스텝마다 물고기를 확인하는 로직
# 사실 구현문제라.. BFS 를 사용한 것 말고는 다른 특이점은 없다.
