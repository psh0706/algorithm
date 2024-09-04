import sys

def solution():
    n = 9
    dwarves = sorted(list(map(int, [sys.stdin.readline().strip() for _ in range(n)])))
    totalSum = sum(dwarves)

    fakeDwarveIndexes = []
    for i in range(n):
        for j in range(n):
            if j <= i: continue
            else:
                if (totalSum - (dwarves[i] + dwarves[j])) == 100:
                    fakeDwarveIndexes = [i, j]
                    break

        if len(fakeDwarveIndexes) > 0 : break

    for k in range(n):
        if k in fakeDwarveIndexes:
            continue
        else:
            print(dwarves[k])


solution();

# 그냥 구현 문제