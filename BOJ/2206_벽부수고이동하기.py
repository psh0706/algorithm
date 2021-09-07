import sys

N, M = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
visit = [[[False, False] for _ in range(M)] for _ in range(N)]
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def BOJ2206():
    cnt = 1
    q = []

    visit[0][0][1] = True
    q.append([0, 0, 1])

    while len(q) != 0:
        size = len(q)
        for _ in range(size):
            n = q.pop(0)

            if n[0]+1 == N and n[1]+1 == M:
                return cnt

            for d in delta:
                dx = n[0] + d[0]
                dy = n[1] + d[1]
                flag = n[2]

                if 0 > dx or dx >= N or 0 > dy or dy >= M:
                    continue

                if not visit[dx][dy][flag]:
                    if MAP[dx][dy] != 1:
                        visit[dx][dy][flag] = True
                        q.append([dx, dy, flag])
                    else:
                        if flag == 1:
                            visit[dx][dy][1] = True
                            q.append([dx, dy, flag - 1])

        cnt += 1
    return -1


print(BOJ2206())


# 벽을 한번 부순 케이스가 벽을 부수지 않은 케이스의 자리를 선점해버리며 최단거리를 찾아내지 못하는 문제 발생
# 방문처리를 벽을 부순케이스와, 부수지 않은 케이스로 나누어 처리하는것으로 해결
# 상태가 다른 경우 같은 방문처리를 사용하면 안된다는걸 알게되었다.

