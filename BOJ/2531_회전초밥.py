import sys

N, d, k, c = map(int, sys.stdin.readline().split())
rail = [int(sys.stdin.readline()) for _ in range(N)]
rail += rail[0:k-1]
dishKinds = [0 for _ in range(0, d+1)]
maxi = 0
cnt = 0
useCoupon = 0

for i in rail[0:k-1]:
    if dishKinds[i] == 0:
        cnt += 1
    dishKinds[i] += 1

for i in range(k-1, len(rail)):

    if dishKinds[rail[i]] == 0:
        cnt += 1
    dishKinds[rail[i]] += 1

    if dishKinds[c] == 0:
        useCoupon += 1

    if maxi < cnt+useCoupon:
        maxi = cnt+useCoupon

    dishKinds[rail[i - (k - 1)]] -= 1
    useCoupon = 0
    if dishKinds[rail[i - (k - 1)]] == 0:
        cnt -= 1


print(maxi)

