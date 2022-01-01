N, C = map(int,input().split())
li = []
M = int(input())
for _ in range(M):
    li.append(list(map(int, input().split())))

truck = [C for _ in range(N)]
li.sort(key=lambda x: (x[1], x[0]))
cnt = 0
for i in range(M):
    idx1 = li[i][0] - 1
    idx2 = li[i][1] - 1
    temp = min(truck[idx1:idx2] + [li[i][2]])
    if temp == 0:
        continue
    else:
        for j in range(idx1, idx2):
            truck[j] = truck[j] - temp
        cnt += temp

print(cnt)


"""
1. 도착 순서대로 정렬하기 (빨리 싣고 "내리는것"이 가장 많이 배달하는 방법이다.)
    도착 순서가 우선순위
2. 정렬한 대로 순회하면서 truck 을 점유
3. 구간 내에 넣을 수 있는 가장 작은 수를 기준으로
   트럭에 넣을 수 있는지 없는지를 파악 
   -> 넣을 수 없는 경우 (0 인경우) 가 아니라면 물건을 쪼개어 넣고 구간내에 모든 순서 차감
"""