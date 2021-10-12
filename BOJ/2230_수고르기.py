N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]
A.sort()

left, right = 0, 1
Min = 20000000000
while right < N and left < N:
    gap = A[right] - A[left]

    if gap == M:
        Min = gap
        break

    if gap > M:
        Min = min(gap, Min)
        left += 1
        continue
    else:
        right += 1
        continue

print(Min)

"""
투포인터 문제
정렬한 배열을 기준으로 두개의 포인터를 이동시키며 그 차이를 계산하는데
차이가 M 이상인 것 중 가장 작은것을 찾아야하므로 아래와 같다. 

1. M == gap 이면 조건에 맞는 가장 작은 값이므로 멈춘다.
2. M < gap 이면 그 차이를 줄이기 위해 left 를 당긴다.
3. M > gap 이면 조건에 맞지 않으므로 차이를 늘이기 위해 right 를 민다.

위와 같은 과정을 거쳐 조건에 맞는 값을 출력한다.
"""