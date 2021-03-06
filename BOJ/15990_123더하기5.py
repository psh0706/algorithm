T = int(input())
N = [int(input()) for _ in range(T)]

dp = [[0 for _ in range(3)] for _ in range(100001)]

dp[1][0] = 1
dp[2][1] = 1
dp[3][0], dp[3][1], dp[3][2] = 1, 1, 1

for i in range(4, 100001):
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % 1000000009
    dp[i][1] = (dp[i - 2][0] + dp[i - 2][2]) % 1000000009
    dp[i][2] = (dp[i - 3][0] + dp[i - 3][1]) % 1000000009

for t in range(T):
    print(sum(dp[N[t]]) % 1000000009)

"""
항상 조합의 마지막에 더한다 (+1, +2, +3 한다).
+1 한 조합들의 뒤에는 +1 이 오면 안된다.
+2 한 조합들의 뒤에는 +2 가 오면 안된다.
+3 한 조합들의 뒤에는 +3 이 오면 안된다.
=> +1+1, +2+2, +3+3 등 연속되기 때문.

예를들어 5를 1, 2, 3으로 더한 경우의 수를 찾아내고 싶을때이다.
(같은수가 두번이상 연속적으로 반복되면 안된다는 조건)

+1 을 붙혀 방법 만들기
=> 4를 만들 수 있는 방법들에 +1 만 하면 5를 만들 수 있다.
   4를 만들 수 있는 전체 경우의 수 - +1을 붙혀 4를 만들 수 있는 경우의수
=> 4를 만들 수 있는 경우들
   1+2+(1) -- 제외
   3+(1) -- 제외
   1+(3)
=> 1개 가능 (1+3+(1))

+2 를 붙혀 방법 만들기
=> 3을 만들 수 있는 방법들에 +2 만 하면 5를 만들 수 있다.
   3을 만들 수 있는 전체 경우의 수 - 2를 붙혀 3을 만들 수 있는 경우의 수
=> 3을 만들 수 있는 경우들
   2+(1)
   1+(2) -- 제외
   (3)
=> 2개 가능 (2+1+(2), 3+(2))

+3 을 붙혀 방법 만들기
=> 2를 만들 수 있는 방법들에 +3만 하면 5를 만들 수 있다.
   2를 만들 수 있는 전체 경우의 수 - 2를 붙혀 3을 만들 수 있는 경우의 수
=> 2를 만들 수 있는 경우들
   (2)
=> 1개 가능 (2+(3))

5를 나타내는 방법 총 4개
1+3+(1), 2+1+(2), 3+(2), 2+(3)


+)추가
1000000009로 나누어주지 않아서 각 연산마다 나머지 연산을 넣어주었는데 틀림
=> 나머지 연산의 분배법칙이 맞긴한데 그것들을 더할 때 역시 똑같이 나누어 주어야 한다.
   더한게 1000000009를 넘을 수도 있기 때문 << 중요
"""