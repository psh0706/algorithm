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
