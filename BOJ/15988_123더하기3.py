T = int(input())

result = ''

for _ in range(T):
    N = int(input())

    if N < 3:
        result += str(N)+"\n"
    else:
        arr = [0 for _ in range(N+1)]
        arr[0] = 1
        arr[1] = 1
        arr[2] = 2

        for i in range(3, N+1):
            arr[i] = (arr[i-1]+arr[i-2]+arr[i-3])%1000000009

        result += str(arr[-1]) + "\n"

print(result)

"""
9095 1, 2, 3 더하기 문제와 같은 문제
테스트케이스의 범위가 좀 더 크다.
"""