import heapq
N = int(input())
lectures = [list(map(int, input().split())) for _ in range(N)]
lectures.sort(key=lambda x: (x[0], x[1]))
maxi = 1
pq = []
for lecture in lectures:
    while (len(pq) != 0) and (pq[0] <= lecture[0]):
        heapq.heappop(pq)

    heapq.heappush(pq, lecture[1])
    maxi = max(maxi, len(pq))

print(maxi)

"""
N = int(input())
lectures = [list(map(int, input().split())) for _ in range(N)]
table = sum(lectures, [])
table = list(set(table))
table.sort()
time = dict()

for i in range(len(table)):
    time[table[i]] = i
    table[i] = 0

for lec in lectures:
    s = time[lec[0]]
    t = time[lec[1]]

    for i in range(s, t):
        table[i] += 1

print(max(table))
"""

"""
1. 강의를 시작 시간 기준으로 오름차순 정렬한다.
2. 우선순위 큐를 이용해 강의실 개수를 찾는다. (최소힙 - 끝나는 시간 기준)
    2-1. A 강의의 시작시간이 우선순위큐의 root (= 가장 빨리 끝나는 강의) 보다 크면 
         A 강의의 시작 시간보다 큰 시간이 나올 때 까지 우선순위큐를 Pop 하고, 강의 A의 끝나는 시간을 push 한다.
    2-2. 만약 A의 시작시간이 우선순위큐의 root 보다 작으면 강의 A의 끝나는 시간을 push 한다.
    2-3. 과정 중 가장 요소의 갯수가 많았을 때가 강의실의 갯수이다.
"""