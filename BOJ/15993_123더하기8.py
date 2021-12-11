n = int(input())
cases = [int(input()) for _ in range(n)]
dp = [[0 for _ in range(2)] for _ in range(100001)]
dp[1][1] = 1
dp[2][0] = 1
dp[2][1] = 1
dp[3][0] = 2
dp[3][1] = 2

for i in range(4, 100001):
    dp[i][0] = (dp[i - 1][1] + dp[i - 2][1] + dp[i - 3][1]) % 1000000009
    dp[i][1] = (dp[i - 1][0] + dp[i - 2][0] + dp[i - 3][0]) % 1000000009

for case in cases:
    print(str(dp[case][1]) + " " + str(dp[case][0]))

"""
홀수개 + 1개 => 짝수
짝수개 + 1개 => 홀수
임을 이용하였다.

5의 짝수개 조합 => 4의 홀수개조합 + 3의 홀수개 조합 + 2의 홀수개 조합
5의 홀수개 조합 => 4의 짝수개조합 + 3의 짝수개 조합 + 2의 짝수개 조합
"""