def checkMatrix(a, b):
    n = len(a)
    for line in range(n):
        if a[line] != b[line]:
            return False
    return True


def solution():
    n, m = map(int, input().split())
    matrixA = [list(map(int, list(input())))for _ in range(n)]
    matrixB = [list(map(int, list(input()))) for _ in range(n)]
    cnt = 0

    if n >= 3 and m >= 3:
        for x in range(0, n-2):
            for y in range(0, m-2):
                if matrixA[x][y] == matrixB[x][y]:
                    continue

                cnt += 1

                for i in range(x, x+3):
                    for j in range(y, y+3):
                        if matrixA[i][j] == 1:
                            matrixA[i][j] = 0
                        else:
                            matrixA[i][j] = 1

    if checkMatrix(matrixA, matrixB):
        print(cnt)
    else:
        print(-1)


solution()

"""
그리디 문제
행렬의 크기가 연산사이즈(3x3) 보다 작다면, 뒤집기연산을 할수없으므로 별도의 처리를 하지 않는다.
행렬의 크기가 연산사이즈 보다 크면, 뒤집기 연산이 가능한 부분만 순차적으로 맞는지 틀리는지 확인해 나간다.
뒤집기 연산이 가능한 부분의 모든 칸에서
행렬 a의 그 부분과 행렬 b의 그 부분이 같은지를 확인하고 
다르다면 뒤집기 연산을 진행한다.

연산이 끝난 후 a와 b가 같은지 확인하면된다.
"""