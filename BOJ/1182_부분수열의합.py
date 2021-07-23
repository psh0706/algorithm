
N, S = map(int, input().split())
arr = list(map(int, input().split()))

isS = 0

for i in range(1 << N):
    sum = 0

    if i == 0:
        continue

    for j in range(N):
        if i & (1 << j):
            sum += arr[j]

    if sum == S:
        isS += 1

print(isS)

