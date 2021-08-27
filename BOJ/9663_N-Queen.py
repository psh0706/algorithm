import sys


def check(i, j):
    for q in range(i):
        if j == Queen[q]:
            return False
        elif abs(i - q) == abs(j - Queen[q]):
            return False
    return True


def nQueen(depth):
    if depth == N:
        global result
        result += 1
        return

    for j in range(N):
        if check(depth, j):
            Queen[depth] = j
            nQueen(depth + 1)


N = int(sys.stdin.readline())
Queen = [-1 for _ in range(N)]
result = 0
nQueen(0)
print(result)
