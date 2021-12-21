T = int(input())
nList = []
infoList = []
for _ in range(T):
    nList.append(int(input()))
    infoList.append(list(map(int, input().split())))

for i in range(T):
    n = nList[i]
    info = infoList[i]
    info.insert(0, 0)
    visit = [0 for _ in range(n + 1)]
    ans = 0

    # 모든 학생들을 순회하며 팀 구성 여부를 확인
    for j in range(1, n + 1):
        if visit[j] > 0:
            continue
        cnt = 1
        temp = j
        visit[temp] = 1

        while True:
            temp = info[temp]
            if visit[temp] > 0:
                break
            visit[temp] = 1
            cnt += 1

        if visit[temp] == 1:
            while visit[temp] != 3:
                visit[temp] = 3
                temp = info[temp]
                cnt -= 1

        temp = j
        while visit[temp] == 1:
            visit[temp] = 2
            temp = info[temp]

        ans += cnt
    print(ans)


"""
무방향그래프 (자기 자신을 가리키는게 없고 방향이 없는) 에서는 유니온 파인드 해주면 되는데
이거는 방향그래프라 dfs를 써줘야 한다고함.
방문한 곳을 다시 방문하면 → 회전한 것이다.
"""

"""
이 문제 계속 시간초과 났던 이유는 → 내가 방문을 두개 사용해서 (10만개 짜리 배열을 매번 할당하니깐.)
해결방법: 방문 처리 하나만 이용하고 상태를 방문에 적기

1→ 탐색중
2→ 그룹 아님
3→ 그룹

1. 탐색 하다 ( 1로 바꿔주면서 ) 일단 한번이라도 방문한적 있는 노드에 방문시 stop
2. 그 노드를 기준으로 다시한번 회전하면서 상태를 3으로 바꿔줌.
3. 맨처음 시작했던 노드를 기준으로 다시 돌면서 그룹 만나기 전 까지 다 2로 바꿔줌
   → 왜냐면 그 쪽 line은 전부 그 그룹으로 흘러갈거고 그러면 전부 다 안되는 애들이니깐.
"""