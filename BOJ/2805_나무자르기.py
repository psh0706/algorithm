N, M = map(int, input().split())
tree = sorted(map(int, input().split()), reverse=True)


def cutTree(line):

    acc = 0

    for i in range(N):
        if line >= tree[i]:
            break
        else:
            acc += (tree[i] - line)

    return acc


def binarySearch():
    last = 0
    left = 0
    right = max(tree)

    while left <= right:
        mid = int((left + right) / 2)
        meter = cutTree(mid)

        if meter >= M:
            last = mid
            left = mid + 1
        else:
            right = mid - 1

    return last


print(binarySearch())


"""
나무를 mid 만큼 잘랐을 때 총 몇 m를 얻을 수 있는지 이분탐색하며 찾아 나간다.
얻어야 하는 나무보다 더 많이 얻어진다면 거기 까지는 조건을 충족하므로 mid 를 last 에 저장한뒤 다시 이분탐색하고.
얻어야 하는 나무보다 덜 얻어진다면 조건을 충족하지 않으므로 그냥 다시 이분탐색을 진행한다.
left 가 right 보다 커지는 순간 (이분탐색이 끝난 순간)의 last 가 최대로 얻을수 있는 meter 값이 된다.
"""

