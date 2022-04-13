m = int(input())
n = int(input())
prime = []

arr = [False for _ in range(n+1)]
for i in range(2, n + 1):
    if not arr[i]:
        if m <= i <= n:
            prime.append(i)
        multiple = 2
        while True:
            if i * multiple > n:
                break
            arr[i * multiple] = True
            multiple += 1
    else:
        continue

if not prime:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))

"""
에라토스테네스의 체를 이용해 소수를 구하는 문제
"""