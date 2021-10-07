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

"""
조카들에게 나눠줄 과자의 길이를 기준으로 이분탐색을 한다.
과자의 길이는 양수 이므로
1 ~ 최대과자길이 사이를 이분탐색하는데,
조카 3명과 10, 10, 15 의 과자가 있고 이분탐색의 mid 값이 (= 나눠줄 과자 길이가) 7일 경우
7, 7, 7, 7, 3, 3, 1 로 나누어질 수 있다.
(10/7)*2 + (15/2)*1
길이 7 짜리 과자가 4개 이므로 조카의 수 보다 많고, 이것은 조건에 부합한다.
따라서 길이가 7일 때는 무조건 된다는 이야기 이므로 결과를 저장하고 >> 길이를 높혀서 위의 과정을 반복한다.
반대로 조건에 부합하지 않을 때는 길이를 낮추어 위의 과정을 반복하면 된다.
"""