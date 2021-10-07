K, N = map(int, input().split())
LAN = [int(input()) for _ in range(K)]

low = 1
high = max(LAN)
result = 0
while low <= high:
    mid = int((low + high)/2)

    count = sum([(x//mid) for x in LAN])

    if count >= N:
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)

"""
16401 과자 나눠주기 문제와 같은 풀이
코드를 좀 더 간결하게 짜 보았다!
"""