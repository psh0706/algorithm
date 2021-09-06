import sys

N, K = map(int, sys.stdin.readline().split())
bottles = []
cnt = 0
share = N
x = 1

while share != 0:
    remainder = share % 2
    share = int(share / 2)

    if remainder == 1:
        bottles.append(x)

    x *= 2

while True:

    if len(bottles) <= K:
        break

    flag = True
    for i in range(0, len(bottles)-1):
        if bottles[i] == bottles[i+1]:
            bottles.append(bottles[i] * 2)
            del bottles[i:i+2]
            bottles = sorted(bottles)
            flag = False
            break
        else:
            continue

    if flag:
        cnt += bottles[0]
        bottles.insert(0, bottles[0])


print(cnt)
