n, m = map(int, input().split())
arr = [0 for _ in range(n+1)]


def recursion(n):
    if n == 1:
        arr[1] = 1
        return 1

    arr[n] = n * recursion(n - 1)
    return arr[n]


if n == m:
    print(1)
else:
    recursion(n)
    combination = arr[n] // (arr[n - m] * arr[m])
    print(int(combination))


"""
조합 개수를 구하는 문제 (nCm)
배열에 팩토리얼 값을 저장했다가 접근하는 방식으로 문제를 풀었다.
처음엔 18번 line 을 / (= 실수나누기) 후 integer 로 형 변환 하는 것을 구현했다가 틀렸다.
아무래도 큰 수가 들어가며 오차가 생긴듯 했다. // (= 정수나누기) 로 수정하니 빠른 속도로 문제를 풀 수 있었다.
"""

