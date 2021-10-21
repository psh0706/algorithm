import copy
import itertools

N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
moveList = itertools.product([1, 2, 3, 4], repeat=5)


def main():
    maxVal = 0
    for move in moveList:
        clone = copy.deepcopy(MAP)
        for m in move:
            if m == 1:
                clone = up(clone)
            elif m == 2:
                clone = down(clone)
            elif m == 3:
                clone = left(clone)
            else:
                clone = right(clone)

        maxVal = max(max(map(max, clone)), maxVal)

    return maxVal


def up(M):
    for c in range(N):
        i, j = 0, 1
        while True:
            if j >= N:
                break

            if M[i][c] == 0:
                if M[j][c] == 0:
                    j += 1
                    continue

                temp = M[j][c]
                M[j][c] = 0
                M[i][c] = temp
                j = i + 1
            else:
                if M[j][c] == 0:
                    j += 1
                    continue

                if M[i][c] == M[j][c]:
                    M[i][c] *= 2
                    M[j][c] = 0
                    i += 1
                    j = i + 1
                else:
                    temp = M[j][c]
                    M[j][c] = 0
                    M[i + 1][c] = temp
                    i += 1
                    j = i + 1

    return M


def down(M):
    for c in range(N):
        i, j = N-1, N-2
        while True:
            if j < 0:
                break

            if M[i][c] == 0:
                if M[j][c] == 0:
                    j -= 1
                    continue

                temp = M[j][c]
                M[j][c] = 0
                M[i][c] = temp
                j = i - 1
            else:
                if M[j][c] == 0:
                    j -= 1
                    continue

                if M[i][c] == M[j][c]:
                    M[i][c] *= 2
                    M[j][c] = 0
                    i -= 1
                    j = i - 1
                else:
                    temp = M[j][c]
                    M[j][c] = 0
                    M[i - 1][c] = temp
                    i -= 1
                    j = i - 1

    return M


def left(M):
    for r in range(N):
        i, j = 0, 1
        while True:
            if j >= N:
                break

            if M[r][i] == 0:
                if M[r][j] == 0:
                    j += 1
                    continue

                temp = M[r][j]
                M[r][j] = 0
                M[r][i] = temp
                j = i + 1
            else:
                if M[r][j] == 0:
                    j += 1
                    continue

                if M[r][i] == M[r][j]:
                    M[r][i] *= 2
                    M[r][j] = 0
                    i += 1
                    j = i + 1
                else:
                    temp = M[r][j]
                    M[r][j] = 0
                    M[r][i + 1] = temp
                    i += 1
                    j = i + 1

    return M


def right(M):
    for c in range(N):
        i, j = N-1, N-2
        while True:
            if j < 0:
                break

            if M[c][i] == 0:
                if M[c][j] == 0:
                    j -= 1
                    continue

                temp = M[c][j]
                M[c][j] = 0
                M[c][i] = temp
                j = i - 1
            else:
                if M[c][j] == 0:
                    j -= 1
                    continue

                if M[c][i] == M[c][j]:
                    M[c][i] *= 2
                    M[c][j] = 0
                    i -= 1
                    j = i - 1
                else:
                    temp = M[c][j]
                    M[c][j] = 0
                    M[c][i - 1] = temp
                    i -= 1
                    j = i - 1

    return M


print(main())

"""
빡구현 문제 2048!
최대 다섯번을 이동했을 때 가장 큰 타일값을 출력하는 문제.

큰 흐름은 다음과 같다.
1. 다섯번을 이동하는 경우의 수 만들기 (moveList)
2. 각 이동을 수행했을 때 최대 타일값 구하기
3. 지금까지 구해진 최대 타일값과 2번에서 구해진 타일값을 비교하여 큰 값으로 maxVal 업데이트

상, 하, 좌, 우로 이동하는 방법은 다음과 같다.
핵심은 N * N 타일을 N개의 라인으로 쪼개어 생각하는것.
투포인터로 각 라인을 계산하면 된다.

"""
