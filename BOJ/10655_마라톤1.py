N = int(input())
checkPoints = []
dists = []
for _ in range(N):
    x1, y1 = map(int, input().split())
    if len(checkPoints) > 0:
        x2, y2 = checkPoints[-1][0], checkPoints[-1][1]
        dists.append(abs(x1 - x2) + abs(y1 - y2))
    checkPoints.append([x1, y1])

total = sum(dists)
mini = 10000000000
for i in range(1, N-1):
    temp = total - dists[i-1] - dists[i]
    x1, y1 = checkPoints[i-1]
    x2, y2 = checkPoints[i+1]
    d = abs(x1-x2)+abs(y1-y2)
    temp += d
    mini = min(mini, temp)


print(mini)

"""
우선 모든 체크포인트간의 거리를 구해둔다.
1-2-3-4 에서 2를 지나친다고 했을 때
1-2 와 2-3 거리를 총 거리의 합(total) 에서 빼고
1-3 거리를 새롭게 구해 더해주는 방식으로 탐색을 진행하면 O(n)으로 문제를 풀 수 있다.
2중 반복문을 사용하는 순간 시간복잡도가 최대 100000^2 가 되므로 시간초과를 유의해야한다.
"""