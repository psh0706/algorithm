import heapq
import time
from itertools import permutations

delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def checkWeight(numDirty, edgeInfo, dirty, w, h, room):
    Edge = dict()
    for a in range(numDirty):
        Edge[a] = dict()
        for b in range(numDirty):
            if not edgeInfo[a][b]:
                continue

            # bfs 로 weight 측정
            destX, destY = dirty[b][0], dirty[b][1]
            visit = [[False for _ in range(w)] for _ in range(h)]
            visit[dirty[a][0]][dirty[a][1]] = True
            q = [[dirty[a][0], dirty[a][1]]]
            flag = False
            acc = 0
            while q:
                size = len(q)
                acc += 1
                for _ in range(size):
                    n = q.pop(0)
                    for d in delta:
                        dx = n[0] + d[0]
                        dy = n[1] + d[1]

                        if 0 <= dx < h and 0 <= dy < w and not visit[dx][dy] and room[dx][dy] != "x":
                            if dx == destX and dy == destY:
                                Edge[a][b] = acc
                                flag = True
                                break
                            else:
                                q.append([dx, dy])
                                visit[dx][dy] = True
                    if flag:
                        break
                if flag:
                    break
    return Edge


def perm(numDirty, Edge):
    li = list(permutations(range(1, numDirty), numDirty-1))
    mini = int(1e9)
    for case in li:
        acc = Edge[0][case[0]]
        for c in range(len(case)-1):
            acc += Edge[case[c]][case[c+1]]
        mini = min(mini, acc)
    return mini


def main():
    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break
        room = []
        dirty = dict()
        robot = []
        numDirty = 0
        # 0 -> 로봇 청소기
        for i in range(h):
            line = list(input())
            for j in range(w):
                if line[j] == 'o':
                    robot = [i, j]
                elif line[j] == '*':
                    numDirty += 1
                    dirty[numDirty] = [i, j]
            room.append(line)

        if numDirty > 0:
            numDirty += 1
            edgeInfo = []
            for key in dirty:
                temp = []
                for j in range(numDirty):
                    if key == j or j == 0:
                        temp.append(False)
                    else:
                        temp.append(True)
                edgeInfo.append(temp)
            edgeInfo.insert(0, [True for _ in range(numDirty)])
            edgeInfo[0][0] = False
            dirty[0] = robot
            Edge = checkWeight(numDirty, edgeInfo, dirty, w, h, room)
            flag = False
            for key in Edge:
                if not Edge[key]:
                    flag = True
                    break
            if flag:
                print(-1)
            else:
                print(perm(numDirty, Edge))
        else:
            print(0)


main()

"""
은근히 어려웠던 문제..ㅠ
1. 로봇청소기 -> 각 먼지 사이 거리와
   각먼지 -> 각 먼지 사이 거리를 bfs 로 구해주었다.
2. 로봇청소기가 각 먼지사이를 순회하는 순서를 순열을 통해 만들고
   각 경우를 계산해서 최저값을 찾는다.

갠적으로 구현하는게 빡셌던거같다..
나중에 순열이 아니라 비트마스킹을 사용해보는걸로 리팩토링 해보아야겠다.
"""