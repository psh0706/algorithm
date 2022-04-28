n = int(input())
homework = []
maxDay = 0
for i in range(n):
    d, w = map(int, input().split(" "))
    homework.append([d, w])
    maxDay = max(maxDay, d)
homework.sort(key=lambda x: [x[0], x[1]])

daily = [0 for _ in range(maxDay+1)]
for [d, w] in homework:
    daily[d] += 1

for i in range(maxDay-1, 0, -1):
    daily[i] += daily[i+1]

temp = []
answer = 0
visit = [False for _ in range(n)]
for i in range(maxDay, 0, -1):
    for j in range(-daily[i], 0):
        if visit[j]:
            continue

        if not temp:
            visit[j] = True
            temp = [j, homework[j][1]]
            continue

        if temp[1] < homework[j][1]:
            visit[temp[0]] = False
            visit[j] = True
            temp = [j, homework[j][1]]

    if not temp:
        continue
    answer += temp[1]
    temp = []

print(answer)

"""
d 를 마감일로 생각하고, 마감일 까지 할 수 있는 최대값을 골라 나가는 방식을 사용했다.
"""