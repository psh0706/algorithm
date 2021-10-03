N = int(input())
INF = int(1e9)
dp = [i for i in range(N+1)]
dp[0] = 0

for i in range(1, N + 1):
    j = 1
    while True:
        index = i - (j * j)
        if index >= 0:
            dp[i] = min(dp[i], dp[index]+1)
        else:
            break
        j += 1

print(dp[N])

"""
앞에서부터 최적화를 해가며 진행하는 dp 문제
dp[9]는
dp[9-(1^2)], dp[9-(2^2)], dp[9-(3^3)] 중 가장 작은 값에 +1 한 값이다.
자세한 설명은 블로그에 남겨야징
"""