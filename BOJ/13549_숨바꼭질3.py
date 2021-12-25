from collections import deque

N, K = map(int, input().split())
visit = [False for _ in range(100001)]

q = deque([[N, 0]])
visit[N] = True
while len(q) != 0:
    node = q.popleft()
    x = node[0]
    time = node[1]

    if x == K:
        print(time)
        break

    if x * 2 <= 100000 and not visit[x * 2]:
        q.append([x * 2, time])
        visit[x * 2] = True

    if x - 1 >= 0 and not visit[x - 1]:
        q.append([x - 1, time+1])
        visit[x - 1] = True

    if x + 1 <= 100000 and not visit[x + 1]:
        q.append([x + 1, time+1])
        visit[x + 1] = True

"""
1697번 처럼 bfs 로 풀어봄. visit 처리하면서 depth 세기
다시 문제 읽어보니 +1, -1은 1초가 걸리지만 *2인 순간이동은 0초가 걸림 → 단순 뎁스로 해결할수 없음
큐에 값을 넣으면서 시간(time) 도 함께 넣음. [x, time] +1, -1할 때에는 time 을 +1 , 순간이동시에는 time 그대로를 큐에 넣어줌.

1차 런타임에러 → 맨 위에 deque() 임포트를 포함하지 않아서 생김.
2차 틀렸습니다 → 1 2 가 예시임. 내가 기술을 +1, -1, *2 순으로 해서 순간이동한 *2 (0초)가 먼저 나와야 가장 빠른 이동인건데 +1한 것 (1초)이 먼저나와버림
→ 순서를 *2, +1, -1 순으로 배치. 해결!
"""