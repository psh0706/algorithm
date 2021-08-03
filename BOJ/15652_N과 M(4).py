N, M = map(int, input().split())
arr = list()


def overlapPerm2(depth, start):
    if depth == M:
        [print(str(arr[i]), end=" ") for i in range(len(arr))]
        print()
        return

    for i in range(start, N + 1):
        arr.append(i)
        overlapPerm2(depth + 1, i)
        arr.pop()


overlapPerm2(0, 1)
