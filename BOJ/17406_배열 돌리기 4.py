import copy
import itertools


def rotate(r, c, s, arr):
    for i in range(1, s+1):
        temp = arr[r - i][c - i]

        for x in range(r-i, r+i):
            arr[x][c-i] = arr[x+1][c-i]

        for y in range(c-i, c+i):
            arr[r+i][y] = arr[r+i][y+1]

        for x in range(r+i, r-i, -1):
            arr[x][c+i] = arr[x-1][c+i]

        for y in range(c+i, c-i, -1):
            arr[r-i][y] = arr[r-i][y-1]

        arr[r-i][c-i+1] = temp

    return arr


def solution():
    n, m, k = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(n)]
    ops = [list(map(int, input().split())) for _ in range(k)]
    order = list(itertools.permutations(range(k), k))
    answer = 9999

    for idxes in order:
        tempMap = copy.deepcopy(MAP)
        for idx in idxes:
            rotate(ops[idx][0]-1, ops[idx][1]-1, ops[idx][2], tempMap)
        answer = min(answer, min(map(sum, tempMap)))

    return answer


print(solution())

"""
구현문제 배열돌리기
배열 돌리는 부분이 깔끔하게 잘 구현돼서 좋은 것 같다.
"""