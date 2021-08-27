import sys


def operatorInject(depth, result):
    if depth == N - 1:
        global maxi, mini

        if mini > result:
            mini = result
        if maxi < result:
            maxi = result

        return

    for i in range(len(visit)):
        if visit[i] == 0:
            continue

        visit[i] -= 1
        if i == 0:
            operatorInject(depth + 1, result + A[depth + 1])
        elif i == 1:
            operatorInject(depth + 1, result - A[depth + 1])
        elif i == 2:
            operatorInject(depth + 1, result * A[depth + 1])
        else:
            operatorInject(depth + 1, int(result / A[depth + 1]))
        visit[i] += 1


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
visit = list(map(int, sys.stdin.readline().split()))

maxi = -1000000000
mini = 1000000000

operatorInject(0, A[0])

print(maxi)
print(mini)

