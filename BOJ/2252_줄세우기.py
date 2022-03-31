n, m = map(int, input().split())
info = {i: [] for i in range(1, n+1)}
cnt = [0 for _ in range(n+1)]
q = []
answer = []

for _ in range(m):
    s, e = map(int, input().split())
    info[s].append(e)
    cnt[e] += 1

for i in range(1, n+1):
    if cnt[i] == 0:
        q.append(i)

while q:
    node = q.pop(0)
    for nextNode in info[node]:
        cnt[nextNode] -= 1
        if cnt[nextNode] == 0:
            q.append(nextNode)
    answer.append(str(node))

print(' '.join(answer))

"""
처음 풀어본 위상정렬 문제
딱 보자마자 위상정렬 같았다.

1. 연결 정보와 진입차수 정보를 저장한다. 
   a < b 는 a 다음 b 라는것을 의미하고 a -> b 로 간선을 그릴 수 있다.
   이때 b의 진입 차수는 1 증가하는것이다.
   
2. 진입 차수가 0 인 노드(학생) 들을 모두 큐에 넣는다.

3. 위상 정렬을 시작한다.
    큐에서 노드를 하나 pop 하고(=node) 그것과 관련된 간선들을 모두 지운다.
    (진입하는 간선이 없어지므로 향하는 노드의 진입 간선 정보도 -1 해준다.)
    그 결과로 진입 간선이 0개가 된 노드들이 있다면 그것도 큐에 넣어준다.
    node 를 정렬된 리스트로 옮긴다.
    반복
    
이렇게 하면 진입차수가 낮은 노드부터 차례로 정리해 나갈 수 있다. (위상정렬)
"""