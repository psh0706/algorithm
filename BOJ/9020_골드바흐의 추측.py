def sieve(arr):
    for i in range(2, len(arr)):
        if not arr[i]:
            continue
        j = 2
        while True:
            if i * j >= len(arr):
                break
            arr[i*j] = False
            j += 1
    return


def solution():
    T = int(input())
    nList = [int(input()) for _ in range(T)]

    prime = [True for _ in range(10001)]
    prime[0] = False
    prime[1] = False
    sieve(prime)

    for n in nList:
        answer = n
        partition = []

        for i in range(n-1, 1, -1):
            if prime[i] and prime[n-i]:
                gap = abs(n - (2 * i))
                if answer > gap:
                    answer = gap
                    partition = [n-i, i]

        print(' '.join(map(str, partition)))


solution()

"""
1. 에라스토테네스의 체를 이용해 10000 이전의 소수를 모두 구한다.
2. 주어진 n으로 부터 -1씩 빼면서 거꾸로 수를 순회한다.
3. 소수를 발견하면 n 에서 해당 소수를 뺸 값도 소수인지 확인한다.
4. 두 소수의 차가 현재 최소인지 확인한 뒤 2번 부터 다시 시작한다.
5. 모든 과정을 마친 뒤의 파티션을 출력한다.
"""