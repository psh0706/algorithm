N, M = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
acc = arr[0]
cnt = 0
while left < N and right < N:
    if acc == M:
        cnt += 1

    if acc >= M:
        if left + 1 > right:
            right += 1
            if right == N:
                continue
            acc += arr[right]
        acc -= arr[left]
        left += 1
    else:
        right += 1
        if right == N:
            continue
        acc += arr[right]

print(cnt)
"""
1806 부분합 문제와 거의 같은 문제
테스트케이스의 범위가 조금 다른데, 문제는 없다.
"""