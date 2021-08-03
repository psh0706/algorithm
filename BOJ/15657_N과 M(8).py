def perm(depth, start, result):
    if depth == M:
        print(result)
        return

    for i in range(start, N):
        perm(depth+1, i, result+strings[i])


N, M = map(int, input().split())
strings = [str(i)+" " for i in sorted(map(int, input().split()))]
perm(0, 0, '')
