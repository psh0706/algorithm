import copy


def checkCluster(cave, R, C):
    clusters = []
    delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    visit = [[False for _ in range(C)] for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if cave[i][j] != "x" or visit[i][j]:
                continue

            q = [[i, j]]
            cluster = []
            visit[i][j] = True

            while q:
                node = q.pop(0)
                cluster.append(node)

                for d in delta:
                    dx = d[0] + node[0]
                    dy = d[1] + node[1]
                    if 0 <= dx < R and 0 <= dy < C and not visit[dx][dy]:
                        if cave[dx][dy] == "x":
                            visit[dx][dy] = True
                            q.append([dx, dy])
            clusters.append(cluster)
    return clusters


def checkMineral(height, way, cave, C):
    # 상근 공격 : 오 > 왼
    if way == -1:
        for i in range(C-1, -1, -1):
            if cave[height][i] == 'x':
                cave[height][i] = "."
                return True
    # 창영 공격 : 왼 > 오
    else:
        for i in range(C):
            if cave[height][i] == 'x':
                cave[height][i] = "."
                return True
    return False


def checkHeight(cluster, R, cave):
    h = 999

    tempCave = copy.deepcopy(cave)
    for [x, y] in cluster:
        tempCave[x][y] = "."

    for [x, y] in cluster:
        for i in range(1, R - x + 1):
            d = x + i
            if x + i == R:
                h = min(h, i)
                break

            if tempCave[x + i][y] == 'x':
                h = min(h, i)
                break

    return h


def solution():
    R, C = map(int, input().split())
    cave = [list(input()) for _ in range(R)]
    n = int(input())
    attacks = list(map(lambda x: -1 * int(x) + R, input().split()))

    for i in range(n):
        way = 1 if i % 2 == 0 else -1

        if not checkMineral(attacks[i], way, cave, C):
            continue

        clusters = checkCluster(cave, R, C)

        for cluster in clusters:
            h = checkHeight(cluster, R, cave)

            if h == 1:
                continue

            for c in range(len(cluster)):
                x, y = cluster[c][0], cluster[c][1]
                cave[x][y] = "."
                cluster[c][0] += (h - 1)

            for c in range(len(cluster)):
                x, y = cluster[c][0], cluster[c][1]
                cave[x][y] = "x"

    for c in cave:
        print(''.join(c))

    return


solution()


"""
시간이 조금 걸렸지만.. 골드 2 빡구현 문제 2트만에 풀었다 (ㅠㅠ)

<문제가 있었던 부분>
공격 후 bfs 를 통해 미네랄 클러스터를 확인한다.
그 이후 각 클러스터가 밑으로 떨어지기위해, 
바닥이나 다른 클러스터로부터 얼마나 떨어져 있는지 그 최소 높이를 계산하게되는데 (checkHeight)
클러스터의 요소로부터 밑으로 내려가면서 다른 미네랄('x')을 마주치거나, 바닥을 마주쳤을때 그 높이들의 최소값을 취했다.

그런데 문제는 클러스터의 모양이 구멍이 뚤려있거나, 파여있거나 하는 등의 원인으로
클러스터 요소로부터 밑으로 내려가며 마주친 미네랄이 본인 클러스터 내의 미네랄인 경우가 있었고, 그럴 때 잘못된 높이를 측정하게 됌.
그래서 마주친 미네랄이 자신의 클러스터에 속하는 미네랄인지를 확인하는 구문을 넣었는데
( if not [x, y] in cluster: ... )

이부분은 한 번 실행할 때마다 클러스터 요소 k개의 개수만큼 시간복잡도가 계산되므로 (최악: k**2 + a)
이 부분 때문에 시간초과가 발생했다.

<해결>
동굴의 상태와 똑같은 가짜동굴을 deepcopy 를 통해 만들어주었다.
그리고 높이를 탐색할 클러스터를 가짜동굴에서 싹지워버렸다. (밑으로 내려가다 본인 클러스터의 미네랄을 마주치지 않도록) -> 시간복잡도 k
그 다음 클러스터의 각 요소들의 높이를 측정해주었다.
(덕분에 120 line 은 삭제)

총 최악일 때 2k + a 로 시간복잡도 극뽁.

"""