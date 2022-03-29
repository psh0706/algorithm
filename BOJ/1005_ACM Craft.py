def solution():
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        timer = [0] + list(map(int, input().split()))
        outEdge = {i: [] for i in range(1, N+1)}
        inEdge = [0 for _ in range(N+1)]
        cnt = [0 for _ in range(N+1)]
        for _ in range(K):
            out, inn = map(int, input().split())
            outEdge[out] += [inn]
            inEdge[inn] += 1
        w = int(input())

        q = []
        for i in range(1, N+1):
            if inEdge[i] == 0:
                q.append(i)

        while q:
            node = q.pop(0)

            if node == w:
                print(timer[node] + cnt[node])
                break

            for to in outEdge[node]:
                cnt[to] = max(timer[node]+cnt[node], cnt[to])
                inEdge[to] -= 1
                if inEdge[to] == 0:
                    q.append(to)


solution()


"""
위상정렬을 변형한 문제
위상 정렬로 순서를 맞춰 주면서, 걸리는 시간을 계산해 주면 된다.
"""