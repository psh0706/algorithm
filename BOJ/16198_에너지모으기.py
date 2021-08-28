import sys


def Energy(depth, result):

    if depth == N-2:
        global maxi
        if maxi < result:
            maxi = result
        return

    for i in range(1, N-1):
        if not visit[i]:
            continue

        acc = 1
        left = i - 1
        right = i + 1
        while True:
            if left >= 0:
                if visit[left]:
                    acc *= W[left]
                    break
                else:
                    left -= 1
                    continue
            else:
                break

        while True:
            if right < N:
                if visit[right]:
                    acc *= W[right]
                    break
                else:
                    right += 1
                    continue
            else:
                break

        visit[i] = False
        Energy(depth+1, result+acc)
        visit[i] = True


N = int(sys.stdin.readline())
W = list(map(int, sys.stdin.readline().split()))
visit = [True for _ in range(N)]
maxi = 0
Energy(0, 0)
print(maxi)
