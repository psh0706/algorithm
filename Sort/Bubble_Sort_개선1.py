# 입력 받을 요소의 개수
N = int(input())
# 리스트 입력받기
arr = list(map(int, input().split()))

# 각 턴을 N-1 번 시행한다 -> 길이 N인 리스트의 요소를 하나하나 fix 해 나간다.
for _ in range(N - 1):
    # 한 턴 내의 swap 횟수
    cnt = 0

    for j in range(1, N):
        # 인접한 두 요소를 비교
        if arr[j - 1] > arr[j]:
            # swap
            temp = arr[j - 1]
            arr[j - 1] = arr[j]
            arr[j] = temp
            cnt += 1

    # 한 턴에서 swap 이 한번도 이루어지지 않았으면 이미 정렬 되어있음. (정렬이 끝남)
    if cnt == 0:
        break

print(arr)





