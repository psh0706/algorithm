from collections import Counter

M, N = map(int, input().split())
dic = Counter(map(int, input().split()))
result = 0

# 이분탐색
left = 1
right = max(dic)

while left <= right:
    mid = int((left + right) / 2)

    count = dic[mid] if mid in dic else 0

    # mid 보다 긴 것들
    for key in dic:
        if key <= mid:
            continue

        count += int(key/mid) * dic[key]

    if count >= M:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)
