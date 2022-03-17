n = int(input())
m = int(input())
INF = 1E9
table = [[INF for _ in range(n)] for _ in range(n)]

for _ in range(m):
    start, end, value = map(int, input().split())
    if table[start-1][end-1] > value:
        table[start-1][end-1] = value

for node in range(n):
    for i in range(n):
        for j in range(n):
            if i == j or i == node or j == node:
                continue

            table[i][j] = min(table[i][j], table[i][node] + table[node][j])

line = ''
for n1 in range(n):
    for n2 in range(n):
        if table[n1][n2] == INF:
            line += '0 '
            continue

        line += str(table[n1][n2]) + ' '
    line += '\n'

print(line)


"""
플로이드 - 와샬 문제
다익스트라가 한 정점에서 나머지 정점으로의 최단거리를 구하는것이라면
플로이드 와샬은 모든정점에서 모든정점으로의 최단거리를 구하는것.

기본 idea는 어떤 노드 x와, x를 제외한 나머지 노드의 순서쌍에 (a, b)대하여
"노드 a -> b 가 빠른지 vs a -> x -> b 가 빠른지" 비교하여
더 짧은 거리로 갱신해 나가는것이다.
모든 노드에 대해 위와 같이 갱신을 거치게 되면
모든 노드 -> 모든 노드로의 최단거리를 구할 수 있다.

https://blog.naver.com/ndb796/221234427842
"""