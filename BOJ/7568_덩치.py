n = int(input())
person = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    rank = 1

    for j in range(n):
        if i == j:
            continue

        if person[j][0] > person[i][0] and person[j][1] > person[i][1]:
            rank += 1

    print(rank)

"""
단순하게 비교만 하면 되는 문제
"""