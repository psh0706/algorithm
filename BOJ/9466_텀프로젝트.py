from collections import deque

T = int(input())
nList = []
infoList = []
for _ in range(T):
    nList.append(int(input()))
    infoList.append(list(map(int, input().split())))

for i in range(T):
    n = nList[i]
    info = infoList[i]
    # n = 100000
    # info = [1 for _ in range(100000)]
    # info.append(1)
    info.insert(0, 0)
    # 그룹 확인용 visit
    groupVisit = [False for _ in range(n + 1)]
    cnt = 0
    # 모든 학생들을 순회하며 팀 구성 여부를 확인
    for j in range(1, n+1):
        if groupVisit[j]:
            continue

        nomination = info[j]
        group = deque()
        # 지목 확인용 visit
        arrowVisit = [False for _ in range(n + 1)]

        # 같은 사람을 두 번 지목할 때 까지 계속해서 지목해 나가며 그들을 그룹으로 묶는다.
        while True:
            # 같은 사람을 두 번 지목했거나, 이미 그룹에 포함된 사람을 지목했거나.
            if arrowVisit[nomination] or groupVisit[nomination]:
                break

            arrowVisit[nomination] = True
            temp = info[nomination]
            group.append([nomination, temp])
            nomination = temp

        # 맨 처음 지목한 사람이 마지막으로 지목한 (= 두번 지목된) 사람과 같으면 사이클 형성. 그룹 생성.
        if len(group) == 0:
            continue
        elif group[-1][0] == j and group[-1][1] == nomination:
            cnt += len(group)
            for g in group:
                groupVisit[g[0]] = True

    print(n - cnt)

