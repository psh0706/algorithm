import math
from copy import deepcopy


def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]


def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(n, k):
    N = convert(n, k)
    splitN = N.split('0')
    answer = 0

    prime = deepcopy(splitN)
    for i in range(len(splitN)):
        if splitN[i] == '1':
            prime.remove(splitN[i])
        if splitN[i] == '':
            continue
        if not is_prime(int(splitN[i])):
            prime.remove(splitN[i])

    check = deepcopy(prime)
    for i in range(len(prime)-1):
        check.insert(2*(i+1)-1, '0')

    length = len(check)
    for p in prime:
        if p == '':
            continue
        i = check.index(p)

        if (0 < i < (length - 1)) and check[i-1] == "0" and check[i+1] == "0":
            answer += 1
            continue
        elif i < (length - 1) and check[i+1] == "0":
            answer += 1
            continue
        elif i > 0 and check[i-1] == "0":
            answer += 1
            continue
        if len(splitN) == 1:
            answer += 1

    return answer


solution(437674, 3)

