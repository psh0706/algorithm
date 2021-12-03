T = int(input())
N = [int(input()) for _ in range(T)]
for t in range(T):
    n = N[t]
    if n == 1 or n == 2:
        print(n)
    else:
        dp = [[0 for _ in range(3)]for i in range(n+1)]
        dp[1][0], dp[2][0], dp[3][0] = 1, 1, 2
        dp[2][1] = 1
        dp[3][2] = 1

        for i in range(4, n+1):
            dp[i][0] = sum(dp[i-1])
            dp[i][1] = sum(dp[i-2][1:3])
            dp[i][2] = dp[i-3][2]

        print(sum(dp[n]))


"""
손으로 직접 나열해서 점화식을 찾아 풀었다.
2차원 배열로 쉽게 이해할수 있을것 같은데 그방법은 다음에 풀어봐야겠다.
"""

"""
나만의 점화식 찾기.
"""

"""
2차원 테이블로 수정
"""