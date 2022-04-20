S = int(input())
visit = [[-1 for _ in range(1001)] for _ in range(1001)]

q = [[1, 0, 0]]
visit[1][0] = 0

while q:
    value, clipboard, time = q.pop(0)

    # 클립보드 복사
    if visit[value][value] < 0 or visit[value][value] > time + 1:
        visit[value][value] = time + 1
        q.append([value, value, time + 1])

    # 클립보드 붙혀넣기
    if value+clipboard <= 1000:
        if visit[value+clipboard][clipboard] < 0 or (visit[value+clipboard][clipboard] > time + 1):
            visit[value+clipboard][clipboard] = time + 1
            q.append([value+clipboard, clipboard, time + 1])

    # 하나 지우기
    if value - 1 > 1:
        if visit[value - 1][clipboard] < 0 or (visit[value - 1][clipboard] > time + 1):
            visit[value - 1][clipboard] = time + 1
            q.append([value - 1, clipboard, time + 1])


while True:
    n = min(visit[S])
    if n == -1:
        visit[S].remove(-1)
        continue
    else:
        print(n)
        break


"""
BFS 를 이용해 풀어보았다.
화면에 value 개의 이모티콘이 있을 때 할 수 있는 세 가지 방법은 아래와 같다.

1. 현재 화면의 값 value 를 클립보드에 복사
2. 클립보드 값 value 를 화면에 복사
3. 현재 화면의 값 value - 1

한 가지 노드에 대해 위 세 가지 케이스를 BFS 로 펼쳐나갔다.
방문처리는 화면의 값 value 별 클립보드에 복사된 이모티콘의 개수로 했다. ([value][clipboard])
화면의 이모티콘이 n 개 있을 때 단순 time 만을 기준으로 한다면, 클립보드에 복사된 개수는 무시되어지기 때문이다.
"""