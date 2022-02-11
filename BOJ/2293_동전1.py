n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort()
dp = [0 for _ in range(k+1)]
dp[0] = 1

for c in range(n):
    for i in range(1, k+1):
        if i < coins[c]:
            continue
        dp[i] += dp[i - coins[c]]

print(dp[-1])

"""
k원을 기준으로 메모제이션
결과 : 메모리 초과 -> n차원 배열이기때문?
해결 : 1차원 배열로 변경 후, 동전을 기준으로 메모제이션

메모리 제한이 4MB 이므로
k원이 기준일때가 아니라, 정렬된 동전들을 기준으로해서
동전 c로 만들수 있는 경우의 수를 차곡차곡 쌓아간다.
"""