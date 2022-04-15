def setCord(n):
    return 2*(n - 1)


def solution():
    n, k, r = map(int, input().split())
    delta = [[-2, 0], [2, 0], [0, -2], [0, 2]]
    MAP = [[-1 for _ in range(2*n - 1)] for _ in range(2*n - 1)]
    adj = [[False for _ in range(k)] for _ in range(k)]
    cows = []
    answer = 0

    for i in range(r):
        x1, y1, x2, y2 = map(int, input().split())
        x = int(abs(setCord(x1) + setCord(x2)) / 2)
        y = int(abs(setCord(y1) + setCord(y2)) / 2)
        MAP[x][y] = -2

    for i in range(k):
        x, y = map(int, input().split())
        x = setCord(x)
        y = setCord(y)
        MAP[x][y] = i
        cows.append([x, y])

    for i in range(len(cows)):
        q = [cows[i]]
        visit = [[False for _ in range(2*n - 1)] for _ in range(2*n - 1)]
        visit[cows[i][0]][cows[i][1]] = True
        metCowList = [False for _ in range(k)]

        while q:
            [x, y] = q.pop(0)

            for d in delta:
                dx = x + d[0]
                dy = y + d[1]

                if 0 <= dx < (2*n-1) and 0 <= dy < (2*n-1) and not visit[dx][dy]:
                    if MAP[int((dx+x)/2)][int((dy+y)/2)] == -2:
                        continue
                    if MAP[dx][dy] >= 0:
                        metCowList[MAP[dx][dy]] = True
                    visit[dx][dy] = True
                    q.append([dx, dy])

        for j in range(k):
            if metCowList[j]:
                adj[i][j] = True

    for i in range(k):
        answer += adj[i][i+1:].count(False)

    return answer


print(solution())

"""
BFS 구현문제

1. MAP 을 길이 포함된 사이즈인 (2*n - 1) 사이즈로 늘린다.
2. 소의 위치정보와, 길 정보를 MAP 에 저장. (-1: 빈 칸, -2: 길, 0 이상: 소의 인덱스 번호)
3. 각 소를 기준으로 BFS 하며 만날 수 없는 소의 정보를 adj 배열에 저장.
4. 만나지 않은 소들의 쌍을 count
"""








