N, S = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
result = 100000
acc = arr[0]
flag = False

while left < N and right < N:
    if acc >= S:
        result = min(result, right - left + 1)
        flag = True

        if left + 1 > right:
            right += 1
            if right == N:
                continue
            acc += arr[right]
            continue
        acc -= arr[left]
        left += 1
    else:
        right += 1
        if right == N:
            continue
        acc += arr[right]

if flag:
    print(result)
else:
    print(0)


"""
반례 찾는것이 힘들었던 문제..ㅠ
제한시간이 0.5초로 짧았기 때문에 매번 합연산을 하는 것 보다 포인터를 이동시킬 때 마다 값을 더하거나 빼는 쪽으로 구현하고자 했다.
합 (= acc)

acc >= S: 수열의 left 번째 값을 acc 에서 빼고 left + 1
acc < S: right + 1 한 뒤 수열의 right 번째 값을 acc 에 더하기

반례 때문에 코드가 조금 지저분한데.. 시간이 나면 좀 더 깔끔하게 수정해봐야겠다.
"""
