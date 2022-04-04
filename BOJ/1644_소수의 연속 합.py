def makePrime(N):
    prime = []
    number = [False for _ in range(N+1)]

    for i in range(2, N+1):
        if not number[i]:
            prime.append(i)

            multiple = 2
            while True:
                if i * multiple > N:
                    break
                number[i*multiple] = True
                multiple += 1
        else:
            continue

    return prime


def solution():
    N = int(input())
    arr = makePrime(N)
    length = len(arr)
    answer = 0

    if not arr:
        return 0

    left, right = 0, 0
    temp = arr[0]

    while True:
        if temp <= N:
            if temp == N:
                answer += 1

            if right + 1 < length:
                right += 1
                temp += arr[right]
            else:
                break

        else:
            if left + 1 < length:
                temp -= arr[left]
                left += 1
            else:
                break

    return answer


print(solution())


"""
1. 자연수 N 이하로 나올 수 있는 모든 소수를 구한다 (에라토스테네스의 체 이용)
2. 투포인터로 구간 합을 구하며 구간 합이 N 일때의 경우의 수를 모두 구한다.
"""