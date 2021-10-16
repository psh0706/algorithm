# 입력 받을 요소의 개수
N = int(input())
# 리스트 입력받기
arr = list(map(int, input().split()))

# 각 턴을 N-1 번 시행한다 -> 길이 N인 리스트의 요소를 하나하나 fix 해 나간다.
for i in range(N - 1):
    for j in range(1, N - i):
        # 인접한 두 요소를 비교
        if arr[j - 1] > arr[j]:
            # swap
            temp = arr[j - 1]
            arr[j - 1] = arr[j]
            arr[j] = temp

print(arr)


