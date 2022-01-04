gears = []
for _ in range(4):
    gears.append(list(map(int, list(input()))))

k = int(input())
rotation = [list(map(int, input().split())) for _ in range(k)]

for i in range(k):
    start, how = rotation[i][0] - 1, rotation[i][1]
    q = [[start, how]]
    visit = [2 for _ in range(4)]
    visit[start] = how

    while q:
        [s, h] = q.pop(0)

        # 오른쪽 톱니 바퀴
        if 0 <= s + 1 < 4 and visit[s + 1] == 2:
            if gears[s][2] == gears[s+1][-2]:
                visit[s + 1] = 0
            else:
                visit[s + 1] = -1 * h
                q.append([s+1, -1 * h])

        # 왼쪽 톱니바퀴
        if 0 <= s - 1 < 4 and visit[s - 1] == 2:
            if gears[s][-2] == gears[s - 1][2]:
                visit[s - 1] = 0
            else:
                visit[s - 1] = -1 * h
                q.append([s-1, -1 * h])

    for v in range(4):
        # 반시계
        if visit[v] == -1:
            gears[v].append(gears[v].pop(0))

        # 시계
        elif visit[v] == 1:
            gears[v].insert(0, gears[v].pop())

        else:
            continue

answer = 0
for i in range(4):
    if gears[i][0] == 1:
        answer += 2 ** i
print(answer)


"""
틀렸습니다 이유:
    맨처음 로직을 왼/오 로 나누지 않고 하나의 for 문에서 해결하는것으로 구현했는데
    로직을 왼쪽, 오른쪽으로 나누는 것으로 수정하면서 19번, 27번 if 문속에 continue 를 지우는 것을 깜빡했다..
    오른쪽은 N N 이나 S S 로 같아도 왼쪽은 다를 수 있는데
    왼쪽을 확인 안하고 그냥 넘어가 버린 것.

"""
