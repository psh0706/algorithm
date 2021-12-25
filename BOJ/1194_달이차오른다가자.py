class Node:
    def __init__(self, x, y, inventory, step):
        self.x = x
        self.y = y
        self.inventory = inventory
        self.step = step


R, C = map(int, input().split())
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
MAP = []
startX = 0
startY = 0

for r in range(R):
    line = list(input())
    for c in range(C):
        if line[c] == '0':
            startX = r
            startY = c
            line[c] = '.'
    MAP.append(line)

visit = [[[False for _ in range(C)] for _ in range(R)] for _ in range(64)]
exitFlag = False
answer = -1
q = [Node(startX, startY, 0, 0)]
visit[0][startX][startY] = True

while q:
    n = q.pop(0)

    for d in delta:
        dx = n.x + d[0]
        dy = n.y + d[1]
        tempInventory = n.inventory

        if 0 <= dx < R and 0 <= dy < C:
            if not visit[tempInventory][dx][dy]:
                if MAP[dx][dy] == "#":
                    continue
                if MAP[dx][dy].islower():
                    # 키
                    keyNum = ord(MAP[dx][dy]) - ord('a')
                    tempInventory |= (1 << keyNum)
                    visit[tempInventory][dx][dy] = True
                    q.append(Node(dx, dy, tempInventory, n.step + 1))
                    continue
                if MAP[dx][dy].isupper():
                    # 문
                    keyNum = ord(MAP[dx][dy]) - ord('A')
                    if tempInventory & (1 << keyNum):
                        visit[tempInventory][dx][dy] = True
                        q.append(Node(dx, dy, tempInventory, n.step + 1))
                    continue
                if MAP[dx][dy] == '.':
                    # 길
                    visit[tempInventory][dx][dy] = True
                    q.append(Node(dx, dy, tempInventory, n.step + 1))
                    continue
                if MAP[dx][dy] == '1':
                    # 출구
                    exitFlag = True
                    answer = n.step+1
                    break
    if exitFlag:
        break

print(answer)

"""
방문처리쪽에 문제가 있어서 맨 처음 틀림.
a~f 의 키와 A~F의 문을 매칭하기위해
처음에는 단순히 키를 어떻게 가지고잇는지를 비교만 하려고했다.
방문처리를 가지고 있는 키 자체로해서, 가려는 칸의 방문처리와 내 방문처리가 다르면 이동할수 있게 하려했으나 실패 
→ a, b 가지고 있는거랑 a 가지고 있는것 중 더 많이 가지는 ab 가 우선순위겠지? 

그래서 cnt를 객체에 추가했는데 틀림  
→ a, b 가지는거랑 a 가지는것 중 우선순위는 없음 그냥 다른 상태인 거임 
마찬가지로 a, c, e 가지는거랑 a, b 가지는것울 비교해보아도 그러함. 
단순 cnt 만으로 우선순위를 판단할수는 없다. 
애초에 우선순위가 존재하지않음. 
어떤 키를 가지고, 어떤 경로로 가는지에 따라 출구에 먼저 도착할수도 도착하지 않을 수도 있기 때문임

방문 처리는 갔던 곳을 다시 가지 않기 위함 
→ 상태가 바뀌면 갔던 곳을 다시 갈 수 있어야함.
→ a, b, c, d, e, f, ab, ac, ad, ae, af, abc, abd ...... 총 63가지의 경우를 모두 따져주어야 함을 알수있음.

내가 가지고잇는 키와 64개의 상태를 어떻게 매칭할것인가.
→ 바로 "비트마스킹"

visit 을 64개로 만들어주었다.
각 비짓 안에는 MA P과 같은 크기의 2차원 배열이 들어있고 각 칸은 boolean 타입을 가진다
visit[키 상태][dx][dy] 로 내 상태와 이동할 칸으로 방문처리를 해 주었다.

1. 문 ("A"~"F")
    아스키 코드를 이용해 확인 할 비트의 순번인 keyNum 을 계산하고,
    키를 가지고 있는지 체크하고 방문처리해준다.

    if tempInventory &(1 << keyNum):
        visit[tempInventory][dx][dy]= True
        q.append(Node(dx, dy, tempInventory, n.step + 1))

    
2. 키 ("a" ~ "f")
    아스키 코드를 이용해 추가 할 비트의 순번인 keyNum 을 계산하고,
    인벤토리에 키를 추가해준다.
    
    tempInventory |= (1 << keyNum)
    
3. 벽("#")
    벽은 갈수 없으므로 그냥 넘어간다.
    
4. 출구("1")
    출구를 발견한 순간 out
"""