import copy

N, M = map(int, input().split())

# 진실을 아는 사람들 셋팅
knowTruth = list(map(int, input().split()))
del knowTruth[0]

# 파티 정보 셋팅
Party = []
visit = [False for _ in range(M)]
for _ in range(M):
    party = list(map(int, input().split()))
    del party[0]
    party.sort()
    Party.append(party)

# 진실을 아는 사람이 파티에 있으면 나머지 사람 모두 진실을 아는 사람이 된다.
# 진실을 모르는 사람의 파티만 남을 때 까지 반복한다.
cnt = 0
while cnt != M:

    getToKnow = []

    for p in range(M):
        if visit[p]:
            continue

        people = copy.deepcopy(Party[p])
        for k in knowTruth:
            # k 가 p 에 있는지 찾기
            left, right = 0, len(Party[p]) - 1
            while left <= right:
                mid = int((left + right)/2)
                if Party[p][mid] == k:
                    people.remove(k)
                    break
                if Party[p][mid] > k:
                    right = mid - 1
                else:
                    left = mid + 1

        if len(people) != len(Party[p]):
            getToKnow += people
            visit[p] = True
            cnt += 1
        else:
            continue

    if getToKnow:
        getToKnow = list(set(getToKnow))
        knowTruth = getToKnow
    else:
        break

print(M - cnt)

"""
이분탐색 + 구현문제..!
최대한 deepcopy 를 안 쓰고 싶었는데
직관적으로 이해하기 편한게 좋을것 같아서 그냥 사용했다.

"진실을 아는 사람"이 파티에 있으면 나머지 사람들은 "진실을 알게 된다"는 것이 포인트.

1. 파티를 순회하며 "진실을 아는 사람"이 있는지 확인한다.
2. "진실을 아는 사람"이 있는 파티에 다른 사람들이 있다면(= 진실을 알게 된 사람), "진실을 아는 사람 리스트"에 추가하고 진실을 말해야하는 횟수를 1 증가시킨다.
3. 이것을 더이상 "진실을 알게 된 사람"이 없을 때 까지 반복한다.
4. 총 파티 횟수에서 진실을 말해야 하는 횟수를 뺀다.
"""