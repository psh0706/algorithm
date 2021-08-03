N, M = map(int, input().split())
arr = list()


def perm(depth, start):
    if depth == M:
        [print(str(arr[i]), end=" ") for i in range(len(arr))]
        print()
        return

    for i in range(start, N + 1):
        arr.append(i)
        perm(depth + 1, i + 1)
        arr.pop()


perm(0, 1)
