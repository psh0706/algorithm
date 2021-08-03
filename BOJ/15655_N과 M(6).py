N, M = map(int, input().split())
array = list(map(int, input().split()))
result = list()

# 정렬
array.sort()


def comb(depth, start):
    if depth == M:
        [print(str(result[i]), end=" ") for i in range(len(result))]
        print()
        return

    for i in range(start, N):
        result.append(array[i])
        comb(depth+1, i+1)
        result.pop()


comb(0, 0)
