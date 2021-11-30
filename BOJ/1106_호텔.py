C, N = map(int, input().split())
cost, value = [], []

for _ in range(N):
    c, v = map(int, input().split())
    cost.append(c)
    value.append(v)

dp = [0]
while True:
    if dp[-1] >= C:
        break

    temp = 0
    c = len(dp)
    for i in range(N):
        if c >= cost[i]:
            temp = max(temp, dp[c - cost[i]] + value[i])
    dp.append(temp)

print(len(dp)-1)


"""
도시 = 물건
고객수 = value
비용 = weight (cost)
인 unbounded knapsack 문제로 보아 해결했다.

1,2,3 더하기 문제와 비슷한 방식으로 풀이했다.
한가지 문제는 비용의 한도가 정해져있지 않아서 
dp 테이블을 하나 하나 늘려나가는 방식으로 구현하였다.
"""