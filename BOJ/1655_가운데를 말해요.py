import heapq
import sys

n = int(sys.stdin.readline())
smaller = []
greater = []
result = []

for i in range(n):
    num = int(sys.stdin.readline())

    if len(smaller) == len(greater):
        heapq.heappush(smaller, (-num, num))
    else:
        heapq.heappush(greater, num)

    if greater and smaller[0][1] > greater[0]:
        tempMin = heapq.heappop(greater)
        tempMax = heapq.heappop(smaller)[1]
        heapq.heappush(smaller, (-tempMin, tempMin))
        heapq.heappush(greater, tempMax)

    print(smaller[0][1])

"""
max_heap = 가운데 값보다 같거나 작은 값들의 집합 = smaller
min_heap = 가운데 값보다 큰 값들의 집합 = greater
두 집합을 두고 푼다. 

그냥 집합의 크기(개수)에 맞게 한번은 smaller 집합에, 한번은 greater 집합에 넣어준 뒤
작은 집합에서의 가장 큰 값(tempMax)과 큰 집합에서의 가장 작은 값(tempMin)을 서로 비교한다.
매 번 크기비교를 하는 것이 아니라 덩어리로 생각하는 것.
만약 tempMax 보다 tempMin 이 더 작다면 두 값을 교환해준다.
"""
