from itertools import combinations

arr = [[i, j] for j in range(5) for i in range(5)]
MAP = [list(input()) for _ in range(5)]
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
comb = list(combinations(arr, 7))
answer = 0

for i in range(len(comb)):
    temp = comb[i]
    q = [temp[0]]
    visit = [[False for _ in range(5)] for _ in range(5)]
    visit[temp[0][0]][temp[0][1]] = True
    cnt = 0
    cntY = 0
    while q:
        node = q.pop(0)
        cnt += 1

        if MAP[node[0]][node[1]] == "Y":
            cntY += 1
            if cntY > 3:
                break

        for d in delta:
            dx = node[0] + d[0]
            dy = node[1] + d[1]
            if 0 <= dx < 5 and 0 <= dy < 5 and not visit[dx][dy] and ([dx, dy] in temp):
                visit[dx][dy] = True
                q.append([dx, dy])

    if cnt == 7 and cntY <= 3:
        answer += 1

print(answer)

"""
1. 조합을 이용해서 25개의 좌표중 7개를 고르는 경우를 모두 찾아낸다.
2. 각 경우 별 BFS 를 진행해 인접성 여부와 ‘이다솜파’의 학생이 적어도 4명 이상은 반드시 포함되어 있어야 한다는 조건을 확인한다.
    - 이다솜파 학생이 적어도 4명 이상 있다는 것은, ‘임도연파’ 학생이 4명 이상 있으면 안된다는 조건과 같다.

구현과 브루트포스, bfs 가 적절히 합쳐진 문제였다.
"""