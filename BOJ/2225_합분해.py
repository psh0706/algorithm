n, k = map(int, input().split())
dp = [[0 for _ in range(201)] for _ in range(201)]
dp[0] = [1 for _ in range(201)]
for i in range(201):
    dp[i][0] = 1

for i in range(1, 201):
    for j in range(1, 201):
        dp[j][i] = sum(dp[j-1][:i+1]) % 1000000000

print(dp[k-1][n])

"""
오랜만에 풀어본 DP 문제
수식에 0이 포함될 수도 있다는 점을 유의해야한다.
1을 5개의 합으로 나타내기 
=> 1 + 0 + 0 + 0 + 0
"""