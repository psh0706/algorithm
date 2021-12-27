from collections import deque

N, K = map(int, input().split())
visit = [False for _ in range(100001)]
answer = 0
cnt = 0

q = deque([[N, 0]])
visit[N] = True
flag = False
while len(q) != 0:
    size = len(q)
    tempVisit = []
    answer += 1
    for _ in range(size):
        node = q.popleft()
        x = node[0]
        time = node[1]

        if x == K:
            cnt += 1
            continue

        if x * 2 <= 100000 and not visit[x * 2]:
            q.append([x * 2, time+1])
            tempVisit.append(x * 2)

        if x - 1 >= 0 and not visit[x - 1]:
            q.append([x - 1, time+1])
            tempVisit.append(x - 1)

        if x + 1 <= 100000 and not visit[x + 1]:
            q.append([x + 1, time+1])
            tempVisit.append(x + 1)

    if flag:
        break

    for t in tempVisit:
        if t == K:
            flag = True
            break
        if not visit[t]:
            visit[t] = True


print(answer-1)
print(cnt)

"""
1차 시도 -> 노드에 step 을 포함하는 bfs + k 만 방문처리 안 함 + k가 발견되는 step 까지만 bfs
       반례) 1 -> 10 의 결과는 4, 2 근데 4, 1로 출력.. 왜냐면 1 -> 2 -> 4 -> 5 -> 10 인데 1->2 가는 방법이 2개 (*2, +1) 두 가지 경우를 각각 다르게 쳐줘야함.
2차시도 -> 방문처리를 연산별로 3개로 나눔 (+1, -1, *2) 그래서 1 * 2 와 1 + 1를 다른 상태로 판단
      반례) 1 -> 2 까지는 다르지만, 2 -> 4 -> 5 -> 10 은 연산이 모두 같음. 방문 처리 되어버려서 방법이 1차시도와 마찬가지로 1개
3차시도 -> 방문처리를 step 별로 나누었다. 겹치는 경로들을 여러개 허용하면서, 한번의 방문처리만 함. -> 모았다가 방문처리
"""