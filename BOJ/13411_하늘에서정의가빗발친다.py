import math

n = int(input())
targets = [list(map(int, input().split())) for _ in range(n)]
answers = []

for t in range(n):
    answers.append([math.sqrt(targets[t][0]**2 + targets[t][1]**2)/targets[t][2], t+1])

answers.sort(key=lambda x: (x[0]))

for a in answers:
    print(a[1])


"""
거속시 문제!
"""