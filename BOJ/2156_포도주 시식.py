n = int(input())
wine = [int(input()) for _ in range(n)] + [0, 0, 0]
dp = [0 for _ in range(n)] + [0, 0, 0]
dp[0] = wine[0]

for i in range(n):
    dp[i] = max(wine[i] + wine[i-1] + dp[i-3], wine[i] + dp[i-2], dp[i-1])

print(dp[n-1])

"""
dp[i] = i번째 잔 까지 규칙을 지키며 최대로 마실 수 있는 포도주의 양.
3연속 순번으로 포도주를 마시면 안되기 때문에, 다음과 같이 말할 수 있다.

<마신다> 
...(최대) x 0 0
i-3번째 까지 규칙을 지키며 최대로 포도주를 마신다 + i-1번째 포도주를 마신다 + i번째 포도주를 마신다

or
...(최대) x 0
i-2번째 까지 규칙을 지키며 최대로 포도주를 마신다 + i번째 포도주를 마신다

<안마신다>
...(최대) x
i-1번째 까지 규칙을 지키며 최대로 포도주를 마실때의 양과 같다.

i번째 까지 최대로 마실 수 있는 포도주의 양은 (dp[i]는)
위의 세 가지 경우 (마실 때의 경우 두 가지 + 안마실 때의 경우 한가지) 중 가장 큰 값이다.
\
"""