F, S, G, U, D = map(int, input().split())
visit = [-1 for _ in range(F)]
move = [U, -1*D]

q = [[S-1, 0]]
visit[S-1] = 0

while q:
    node = q.pop(0)

    for d in move:
        dx = node[0] + d
        if 0 <= dx < F:
            if (visit[dx] < 0) or (visit[dx] > (node[1] + 1)):
                q.append([dx, node[1] + 1])
                visit[dx] = node[1] + 1

if visit[G-1] == -1:
    print("use the stairs")
else:
    print(visit[G-1])


"""
BFS 를 이용해 완전 탐색하여 최단비용 찾는 문제.
방문처리 기준을 가장 적게 버튼을 눌렀을 때로 잡으면 된다.
어떤 층에 도착했을 때 버튼을 누른 횟수가 기존보다 작을 때만 더 이동할 수 있다.
"""