N, M = map(int, input().split())
arr = list()


def overlapPerm(depth):
    if depth == M:
        [print(str(arr[i]), end=" ") for i in range(len(arr))]
        print()
        return

    for i in range(1, N+1):
        arr.append(i)
        overlapPerm(depth+1)
        arr.pop()


overlapPerm(0)