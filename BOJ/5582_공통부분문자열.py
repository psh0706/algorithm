a = input()
lenA = len(a)
b = input()
lenB = len(b)

dp = [[0 for _ in range(lenB+1)] for _ in range(lenA+1)]
result = 0

for i in range(1, lenA+1):
    for j in range(1, lenB+1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        # else:
        #     dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        result = max(result, dp[i][j])

print(result)


"""
일반 LCS 에 연속성을 더한 문제
비교 문자가 다른 경우를 생각하지 않고 계산하여 테이블 중 가장 큰 값을 고르면 된다.
"""