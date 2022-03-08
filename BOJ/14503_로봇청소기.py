def searchDust(r, c, d, m, n, go, MAP, visit):
    # 반시계 방향으로 먼지를 탐색하는 함수
    nextD = d
    for _ in range(4):
        nextD = 3 if nextD - 1 < 0 else nextD - 1
        dr = r + go[nextD][0]
        dc = c + go[nextD][1]
        if 0 < dr < m - 1 and 0 < dc < n - 1 and not visit[dr][dc]:
            if MAP[dr][dc] == 0:
                return nextD
    return False


def isWall(r, c, d, m, n, back, MAP):
    # 뒤에 벽이 있는지 탐색
    dr = r + back[d][0]
    dc = c + back[d][1]
    if dr == 0 or dr == m - 1 or dc == 0 or dc == n - 1 or MAP[dr][dc] == 1:
        return True
    return False


def solution():
    m, n = map(int, input().split())
    r, c, d = map(int, input().split())
    back = [[1, 0], [0, -1], [-1, 0], [0, 1]]
    go = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    visit = [[False for _ in range(n)] for _ in range(m)]

    # 1은 벽, 0은 빈공간(청소할 공간)
    MAP = [list(map(int, input().split())) for _ in range(m)]
    cleanArea = 1
    visit[r][c] = True

    while True:
        # 먼지 탐색
        head = searchDust(r, c, d, m, n, go, MAP, visit)
        if type(head) == int:
            # 먼지 탐색 성공 -> 청소
            d = head
            r += go[d][0]
            c += go[d][1]
            visit[r][c] = True
            cleanArea += 1
            continue
        else:
            # 먼지 탐색 실패 -> 이동 가능 여부 탐색
            if not isWall(r, c, d, m, n, back, MAP):
                r += back[d][0]
                c += back[d][1]
                continue
            else:
                break

    print(cleanArea)


solution()


"""
1차 : WA 
-> 뒤로가기 (isWall 함수)에서, 테두리 벽만 탐지하고, 맵중간의 벽은 탐지하지 못함
-> MAP[dr][dc] == 1 이라는 조건을 추가해줌으로써 해결 완료

2차 : AC
-> 전체적으로 문제풀이전 구조화를 잘 했으나, 테스트케이스를 확인하는 과정에서 시간이 조금 소요됨.
-> 테스트케이스를 확인하는 시간 자체를 줄이고 테스트케이스를 만들어보는 연습이 좀 더 필요하다는 생각이 들었던 문제.

"""