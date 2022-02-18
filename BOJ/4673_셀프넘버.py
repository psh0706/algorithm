visit = [False for _ in range(10001)]
for i in range(1, 10001):
    arr = list(map(int, str(i)))
    acc = sum(arr)+i
    if acc <= 10000:
        visit[acc] = True

for i in range(1, 10001):
    if not visit[i]:
        print(i)

"""
1부터 10000까지의 boolean 배열을 이용해 방문처리하는 방식을 이용했다.
1부터 10000까지 반복문을 이용해 d(n)을 실행하고 그 값을 방문처리 하여
방문이 되지 않은 값(= 셀프넘버) 만을 출력한다.
"""