n = int(input())
cards = list(map(int, input().split()))
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(n):
        if j+1 > i:
            break
        dp[i] = max(dp[i], dp[i - (j+1)] + cards[j])

print(dp[-1])

"""
item 을 무한정으로 담을 수 있는 knapsack 문제.
장수를 weight 로, 가격을 value 로 두고 풀었다.
장수가 1개일 때 부터 n개일 때 까지 dp 테이블을 채워가면 된다.
(dp 테이블은 0으로 초기화 한다.)

dp[n] = max(w[n-i]+v[i], dp[n]) (0 <= i <= n)
"""