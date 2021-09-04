import sys

N, K = map(int, sys.stdin.readline().split())
q = [N]
visit = [True for _ in range(100001)]
visit[N] = False


def HideSeek():
    cnt = 0

    while len(q) != 0:
        sec = len(q)

        for i in range(0, sec):
            node = q.pop(0)

            if node == K:
                return cnt
            else:
                if node-1 >= 0 and visit[node-1]:
                    visit[node-1] = False
                    q.append(node - 1)

                if node+1 <= 100000 and visit[node+1]:
                    visit[node+1] = False
                    q.append(node + 1)

                if node*2 <= 100000 and visit[node*2]:
                    visit[node*2] = False
                    q.append(node * 2)

        cnt += 1


print(HideSeek())
