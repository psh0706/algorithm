N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

dp = [0 for _ in range(100)]

for i in range(N):
    for j in range(99, -1, -1):
        if j - L[i] >= 0:
            dp[j] = max(dp[j], dp[j - L[i]]+J[i])


print(dp[-1])

"""
0-1 knapsack 문제
체력 100 을 가방의 크기로 보고
인사를 할 때마다 잃는 체력은 weight, 얻는 기쁨은 value 로 보면 풀 수 있다.
"""