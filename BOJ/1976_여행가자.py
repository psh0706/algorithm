N = int(input())
M = int(input())
MAP = []
for i in range(N):
    MAP.append(list(map(int, input().split())))

plan = list(map(int, input().split()))
for i in range(len(plan)):
    plan[i] -= 1

answer = 'YES'

for i in range(len(plan)-1):
    visit = [False for _ in range(N)]
    q = [plan[i]]
    visit[plan[i]] = True

    flag = False
    while q:
        size = len(q)
        for _ in range(size):
            city = q.pop(0)
            if city == plan[i+1]:
                flag = True
                break

            for j in range(N):
                if MAP[city][j] == 1 and not visit[j]:
                    if plan[i+1] == j:
                        flag = True
                        break
                    else:
                        q.append(j)
                        visit[j] = True

            if flag:
                break
        if flag:
            break

    if not flag:
        answer = "NO"
        break


print(answer)


"""
bfs 응용으로 풀어본 문제
436ms 로 맞고나서 다른분들 풀이를 보니
union-find 로 풀이하신분들도 많았다
나중에 union-find 로도 풀어봐야지
"""