import copy

H, W = map(int, input().split())
walls = list(map(int, input().split()))
rain = [0 for _ in range(len(walls))]
wallMax = [0 for _ in range(len(walls))]

# 왼쪽 -> 오른쪽 벽의 최대 높이 저장하기
maxi = 0
for i in range(len(walls)):
    maxi = max(maxi, walls[i])
    rain[i] = maxi


# 오른쪽 -> 왼쪽 벽의 최대 높이 저장하며 빗물의 높이 계산하기
maxi = 0
for j in range(len(walls)-1, -1, -1):
    maxi = max(maxi, walls[j])
    wallMax[j] = maxi

    if wallMax[j] < rain[j]:
        rain[j] = wallMax[j]

acc = 0
for k in range(len(walls)):
    acc += abs(walls[k] - rain[k])

print(acc)

"""
구현 문제 빗물
오른쪽으로, 왼쪽으로 이동하며 각 경우의 최대 벽 높이를 측정하고
그 차이로 빗물을 계산하도록 했다.
"""