import sys
sys.setrecursionlimit(10**6)


def perm(depth):
    global limit
    if depth == N:
        print("#")
        if limit == 0:
            string = ''
            for i in result:
                string += str(i) + " "
            print(string)
            limit -= 1
        else:
            limit -= 1

        return

    if limit >= 0:
        if check[depth]:
            start = li[depth]
            result[depth] = li[depth]
            visit[li[depth] - 1] = True
            check[depth] = False
            perm(depth+1)
            result[depth] = 0
            visit[li[depth]-1] = False
        else:
            start = 0

        for i in range(start, N):
            if visit[i]:
                continue

            result[depth] = i+1
            visit[i] = True
            perm(depth+1)
            result[depth] = 0
            visit[i] = False


N = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
visit = [False for _ in range(N)]
check = [True for _ in range(N)]
result = [0 for _ in range(N)]
limit = 1
perm(0)
if limit == 0:
    print(-1)

