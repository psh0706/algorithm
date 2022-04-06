n = int(input())
k = int(input()) - 1
sensor = list(set(list(map(int, input().split(" ")))))
sensor.sort()
diff = []

for i in range(len(sensor) - 1):
    diff.append(sensor[i+1] - sensor[i])

diff.sort(key=lambda x: -x)
for _ in range(k):
    if len(diff) == 0:
        break
    diff.pop(0)

if len(diff) > 0:
    print(sum(diff))
else:
    print(0)

"""
각 센서 사이의 거리를 측정하고
가장 먼 거리부터 k-1개 삭제해서 (k-1개를 분리해서) k개의 센서 덩어리를 만든다.
센서와 집중국 간의 거리의 최소값을 구하는 것이기 때문에, 나머지 거리들을 전부 더하면 된다.
중요한것은 n보다 k가 클 수 있다는 점이다 (센서 개수보다 집중국 수가 많을 수 있다.)
"""