import heapq
N = int(input())
li = []

for _ in range(N):
    for num in list(map(int, input().split())):
        heapq.heappush(li, num)
        if len(li) > N:
            heapq.heappop(li)

print(heapq.heappop(li))


"""
(메모리 제한 12MB)
최대로 들어올 수 있는 메모리는 9MB로 
정렬시 사용되는 메모리를 최소화 해야한다. -> 제자리 정렬을 사용해야한다. 우/큐로 힙정렬 사용
근데 그걸써도 터짐ㅋ
그래서 큐 사이즈를 N개로 유지하는 방식으로 진행
"""