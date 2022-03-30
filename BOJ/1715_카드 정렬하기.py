import heapq

n = int(input())
arr = [int(input()) for _ in range(n)]
heapq.heapify(arr)
answer = 0

while len(arr) > 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)

    shake = a + b
    answer += shake
    heapq.heappush(arr, shake)

print(answer)

"""
매 카드 정렬마다 작은값 + 작은값을 하는것이 가장 적은 비용이 든다.
작은 값을 뽑아내기 위해서 heap 자료구조를 이용했다.
"""