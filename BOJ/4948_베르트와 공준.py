arr = []
while True:
    n = int(input())
    if n == 0:
        break
    arr.append(n)

n = max(arr) * 2

erasto = [False for _ in range(n+1)]

for i in range(2, n+1):
    if erasto[i]:
        continue
    j = 2
    while True:
        if i*j > n:
            break
        erasto[i*j] = True
        j += 1

for x in arr:
    print(erasto[x+1:2*x+1].count(False))

"""
에라스토테네스의 체로 소수를 구한 뒤
범위 내의 소수 개수를 count
"""