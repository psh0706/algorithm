n = int(input())
arr = list(map(int, input().split()))
plusArr = [0 for _ in range(n+1)]
MAX = -1000

for i in range(1, n+1):
    plusArr[i] = max(arr[i - 1], plusArr[i - 1] + arr[i - 1])

print(max(plusArr[1:]))


"""
연속된 수의 다양한 누적합들 중 가장 큰 값을 찾아내는 문제 
DP를 이용하면 빠르게 풀 수 있다.
이전까지의 누적합과, 현재 값을 비교해서 큰 값을 찾는것이 포인트

- DP의 누적합
- 다양한 조건이 있는 DP의 누적합
"""