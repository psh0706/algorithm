def makeLIS(arr):
    n = len(arr)
    dp = [1 for _ in range(n)]

    for i in range(1, n):
        MAX = 0
        for j in range(i - 1, -1, -1):
            if arr[i] > arr[j]:
                MAX = max(dp[j], MAX)
            else:
                continue
        dp[i] = MAX + 1
    return dp


def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    DP = makeLIS(arr)
    rDP = makeLIS(list(reversed(arr)))
    MAX = 0

    for i in range(n):
        MAX = max(MAX, DP[i] + rDP[-1*(i+1)] - 1)

    return MAX


print(solution())

"""
정방향으로 LIS 한번, 역방향으로 LIS를 한번 진행해서 각각의 DP테이블을 구해준다.
각 DP[i] 값은 각각 정/역방향으로부터 i번째 요소 까지의 LIS 길이이다.
따라서 어떤 n번째 요소 a에 대해 
a 까지의 정방향 LIS + a 까지의 역방향 LIS - 1(겹치는 것) 을 하면 
a가 Sk (=최고값) 인 바이토닉 부분수열을 구할 수 있다.
이것을 모든 요소에 대해서 수행하고, 가장 길이가 긴 바이토닉 부분 수열을 고르면 된다.

참고로 정방향 i 번째 요소는 역방향 -1*(i+1) 번째 요소와 같다.
"""
