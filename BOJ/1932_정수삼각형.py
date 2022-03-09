n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(len(triangle[i])):
        if 0 > j - 1:
            triangle[i][j] += triangle[i - 1][j]
        elif i - 1 < j:
            triangle[i][j] += triangle[i - 1][j - 1]
        else:
            triangle[i][j] += max(triangle[i - 1][j], triangle[i - 1][j - 1])

print(max(triangle[-1]))


"""
맨 처음에는 DFS 로 접근 -> 시간복잡도가 2*500으로 불가능.
삼각형을 이루는 정점들을 하나하나 확인하며 부모 (왼쪽, 오른쪽, 왼쪽 혹은 오른쪽만 존재하는 경우도 있다.) 중
큰 값을 더해나가는 방식을 이용했다.
"""