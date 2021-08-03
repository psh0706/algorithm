N, M = map(int, input().split())
array = list(map(int, input().split()))
visit = [0 for _ in range(len(array))]
result = list()

# 정렬
array.sort()


# 순열
def perm(depth):
    if depth == M:
        [print(str(result[i]), end=" ") for i in range(len(result))]
        print()
        return

    for i in range(0, N):
        if visit[i] == 1:
            continue

        visit[i] = 1
        result.append(array[i])

        perm(depth + 1)

        visit[i] = 0
        result.pop()


perm(0)
