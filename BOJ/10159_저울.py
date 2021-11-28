N = int(input())
M = int(input())
INF = 1E9
matrix = [[INF for _ in range(N)] for _ in range(N)]

# 그래프 만들어주기
for i in range(N):
    matrix[i][i] = 0

for _ in range(M):
    a, b = map(int, input().split())
    matrix[a - 1][b - 1] = 1
    # matrix[a - 1][b - 1] = 1

# 플로이드-와샬 알고리즘으로 연결 여부 확인하기
# 결과로 도출되는 matrix[i][j]는
# 0보다 크고 INF 보다 작을 때 연결됨을 나타낸다. (값은 몇 다리 건넜는지를 나타낸다)
# 0 은 자기 자신과의 비교, INF 는 연결이 되지 않았음을 의미한다.
for k in range(N):
    for i in range(N):
        if k == i:
            continue
        for j in range(N):
            if k == j:
                continue
            if i == j:
                continue
            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
            # if matrix[i][k] && matrix[k][j]:
            #     matrix[i][j] = True

# 연결 여부 확인
for i in range(N):
    cnt = 0
    for j in range(N):
        # 연결이 안 된 경우만
        if i == j:
            continue
        temp = min(matrix[i][j], matrix[j][i])
        if 0 == temp or temp >= INF:
            cnt += 1
    print(cnt)


"""
플로이드-와샬을 처음 사용해본 알고리즘 문제
다익스트라랑 비슷한 알고리즘인데 이해하는데 시간이 조금 걸렸다.

1. 가중치 인접 행렬을 만든다.
   본 문제에서는 정수값들이 각 노드이고,
   a > b 일 때 a -> b 인 가중치 1의 간선을 가지는
   단방향 그래프로 해석하였다. (a, b는 정수값 = 노드)
   
2. 플로이드-와샬 알고리즘을 통해 연결 여부를 확인해준다.
   예를 들어 1->2, 2->3, 3->4 의 정보가 주어졌을 때 (1 > 2 > 3 > 4 인 관계)
   1번의 과정을 거치고나면 1번 노드의 정보에는 2번 정보만, 2번 노드의 정보에는 3번 정보만, 3번 노드의 정보에는 4번 정보만 기록되지만
   해당 과정을 거치고나면 1->3, 1->4 , 2->4 등의 관계도 확인 할 수 있다.
   (플로이드 와샬이 모든 노드에서 최단 거리를 찾는 알고리즘 이기 때문)
   
3. 갱신된 가중치 인접 행렬를 확인한다.
   연결되지 않은 노드를 발견했을 때 +1 했다.
   
나는 가중치 1의 간선을 가지는 단방향 그래프로 해석해 정통적인 플로이드와샬 알고리즘을 사용했지만,
그냥 간선이 존재 할 때를(boolean) 가중치 인접 행렬에 나타내어 갱신하는 방법도 있다.
(13, 29, 30 line 주석 참고)
"""