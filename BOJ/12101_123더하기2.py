N, k = map(int, input().split())

dp = [1, 1, 2, 4]

if N > 3:
    i = 4
    while True:
        if i == N+1:
            break
        dp.append(dp[i-1] + dp[i-2] + dp[i-3])
        i += 1

if dp[N] < k:
    print(-1)
else:
    index = N
    result = ""
    while index > 0:
        if index - 1 >= 0 and dp[index - 1] >= k:
            result += "1+"
            index -= 1
        elif index - 2 >= 0 and dp[index - 2] >= (k - dp[index - 1]):
            result += "2+"
            k -= dp[index - 1]
            index -= 2
        elif index - 3 >= 0 and dp[index - 3] >= (k - dp[index - 1] - dp[index - 2]):
            result += "3+"
            k -= (dp[index - 1] + dp[index - 2])
            index -= 3

    print(result[:-1])


"""
123 더하기 2번 문제
1번 문제를 응용한 것인데
dp 테이블을 만들어놓고 뒤로 이동하며 1, 2, 3을 적절히 붙혀준다.
"""