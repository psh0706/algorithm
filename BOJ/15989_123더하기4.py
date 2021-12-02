T = int(input())
for _ in range(T):
    n = int(input())
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3

    for i in range(3, n+1):
        dp[i] = dp[i-1] + (dp[i-2] - dp[i-3])
        if i % 3 == 0:
            dp[i] += 1

    print(dp)


"""
손으로 직접 나열해서 점화식을 찾아 풀었다.
2차원 배열로 쉽게 이해할수 있을것 같은데 그방법은 다음에 풀어봐야겠다.
"""
