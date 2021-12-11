n = int(input())
cases = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(1001)] for _ in range(1001)]
dp[1][1] = 1
dp[2][1] = 1
dp[2][2] = 2
dp[3][1] = 1
dp[3][2] = 3
dp[3][3] = 4

for i in range(4, 1001):
    for j in range(2, 1001):
        if i < j:
            break

        dp[i][j] = dp[i][j-1]
        for k in range(1, 4):
            if dp[i - k][j - 1] > 0:
                dp[i][j] = (dp[i][j] + (dp[i-k][j-1] - dp[i-k][j-2])) % 1000000009


for case in cases:
    print(dp[case[0]][case[1]])

"""
1,2,3 더하기 7번을 누적합 형태로 풀어나가는 문제로 이해했다.
그런데 한 테이블에서 해야하므로 식이 조금 바뀌었다.
dp[i][j] - dp[i][j-1] 이 의미하는것은 숫자 i의 조합 중 길이가 j인 것들의 개수이다.
이것을 이용해 일반화 하여 풀었다.

dp[i][j] = 
1전 조합길이 j-1 개수 (dp[i-1][j-1] - dp[i-1][j-2]) +
2전 조합길이 j-1 개수 (dp[i-2][j-1] - dp[i-2][j-2]) +
3전 조합길이 j-1 개수 (dp[i-3][j-1] - dp[i-3][j-2]) +
숫자 i를 j-1길이 이하로 나타낸 개수 (dp[i][j-1])

"""