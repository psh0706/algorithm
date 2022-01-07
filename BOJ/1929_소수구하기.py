m, n = map(int, input().split())
visit = [False for _ in range(n + 1)]
answer = []

for i in range(2, n + 1):
    if visit[i]:
        continue
    if i >= m:
        answer.append(i)

    for j in range(i, n+1, i):
        if not visit[j]:
            visit[j] = True

for a in answer:
    print(a)


"""
에라토스테네스의 체 문제
2부터 각 수의 배수들을 지워나가고 남은 수가 소수이다
"""