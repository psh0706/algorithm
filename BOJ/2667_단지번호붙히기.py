import heapq

n = int(input())
MAP = [list(map(int, list(input()))) for _ in range(n)]
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
visit = [[False for _ in range(n)] for _ in range(n)]
answer = []
for i in range(n):
    for j in range(n):

        if visit[i][j] or MAP[i][j] == 0:
            continue

        q = [[i, j]]
        visit[i][j] = True

        cnt = 1
        while q:
            node = q.pop(0)
            for d in delta:
                dx = node[0] + d[0]
                dy = node[1] + d[1]

                if 0 <= dx < n and 0 <= dy < n and not visit[dx][dy]:
                    if MAP[dx][dy] == 1:
                        cnt += 1
                        visit[dx][dy] = True
                        q.append([dx, dy])
                    else:
                        continue

        heapq.heappush(answer, cnt)

print(len(answer))
for _ in range(len(answer)):
    print(heapq.heappop(answer))


"""
4963번 섬구하기와 같은 문제
출력 부분에서 각 단지내 집의 수를 오름차순으로 출력해야했는데
일반정렬보다 그냥 힙큐(최소힙)를 이용해 삽입하고 루트를 출력하는 방식으로 구현.
"""