# 입력 받을 요소의 개수
N = int(input())
# 리스트 입력받기
arr = list(map(int, input().split()))

# k 를 이용하여 범위제한
k = N
while k > 0:
    last = 0
    # k 번째 인덱스까지 수행
    for j in range(1, k):
        if arr[j-1] > arr[j]:
            temp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = temp
            last = j
    # k 는 마지막으로 swap 된 인덱스
    k = last

print(arr)

