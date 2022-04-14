def solution():
    v, e = map(int, input().split())
    adj = {i: [] for i in range(v)}
    toggle = 1

    for _ in range(e):
        v1, v2 = map(int, input().split())
        v1 -= 1
        v2 -= 1

        adj[v1].append(v2)
        adj[v2].append(v1)

    visit = [-1 for _ in range(v)]

    for i in range(v):
        if visit[i] > -1:
            continue

        q = [i]
        visit[i] = toggle
        temp = []
        while q:
            size = len(q)
            toggle = not toggle

            for _ in range(size):
                node = q.pop(0)

                for j in adj[node]:
                    if visit[j] == toggle:
                        continue
                    elif visit[j] == -1:
                        visit[j] = toggle
                        q.append(j)
                    else:
                        return "NO"
    return "YES"


"""
이분 그래프의 정의를 잘 모르고 풀었다가 다시 푼 문제..
(간선 하나를 지웠을 때 두 개로 나누어질 수 있는 그래프로 이해하고 풀었다)
이분 그래프의 정의는 "인접한 정점끼리 서로 다른 색으로 칠해서 모든 정점을 두 가지 색으로만 칠할 수 있는 그래프" 이므로
BFS 를 이용해서 뎁스 별로 색을 번갈아 칠해주면된다.
이 때 칸이 비어 있다면 이번에 칠해야할 색으로 칠하면 되고,
칠해야 할 색으로 칠해져 있다면 그냥 넘어가면 된다.
하지만 이미 다른 색으로 칠해져 있는 노드를 만난다면
"인접한 정점끼리 서로 다른 색으로 칠한다" 는 조건을 위반한 것이므로 이분 그래프가 아니다.
"""

