N = int(input())
flag = False
T = []
S = []
O = []
MAP = []


def isCatch(t, dic):
    if dic == "u":
        s = dict({'x': 0, 'y': 0})
        o = dict({'x': 0, 'y': 0})
        for item in S:
            if item['y'] == t['y']:
                if item['x'] > s['x']:
                    s = item
        for item in O:
            if item['y'] == t['y']:
                if item['x'] > o['x']:
                    o = item

        if s['x'] < o['x'] < t['x']:
            return True
        else:
            return False
    elif dic == "d":
        s = dict({'x': N, 'y': N})
        o = dict({'x': N, 'y': N})
        for item in S:
            if item['y'] == t['y']:
                if item['x'] < s['x']:
                    s = item
        for item in O:
            if item['y'] == t['y']:
                if item['x'] < o['x']:
                    o = item

        if s['x'] > o['x'] > t['x']:
            return True
        else:
            return False
    elif dic == "l":
        s = dict({'x': 0, 'y': 0})
        o = dict({'x': 0, 'y': 0})
        for item in S:
            if item['x'] == t['x']:
                if item['y'] > s['y']:
                    s = item
        for item in O:
            if item['x'] == t['x']:
                if item['y'] > o['y']:
                    o = item

        if s['y'] < o['y'] < t['y']:
            return True
        else:
            return False
    else:
        s = dict({'x': N, 'y': N})
        o = dict({'x': N, 'y': N})
        for item in S:
            if item['x'] == t['x']:
                if item['y'] < s['y']:
                    s = item
        for item in O:
            if item['x'] == t['x']:
                if item['y'] < o['y']:
                    o = item

        if s['y'] > o['y'] > t['y']:
            return True
        else:
            return False


def recur(depth):
    global flag
    if depth == 3:
        for t in T:
            if isCatch(t, "u") and isCatch(t, "d") and isCatch(t, "l") and isCatch(t, "r"):
                flag = True
                print("YES")
                return
            else:
                return

    for x in range(N):
        for y in range(N):
            if MAP[x][y] != 'X':
                continue

            MAP[x][y] = 'O'
            O.append({'x': x, 'y': y})
            recur(depth+1)
            if flag:
                return
            MAP[x][y] = 'X'
            O.remove({'x': x, 'y': y})


for i in range(N):
    li = list(input().split())
    for j in range(N):
        if li[j] == 'T':
            T.append({'x': i, 'y': j})
        elif li[j] == 'S':
            S.append({'x': i, 'y': j})
    MAP.append(li)
recur(0)
if not flag:
    print("NO")


"""
재귀 + 구현 문제
Object 를 재귀로 3개 배치해주고 
선생님의 시야에 학생이 보이는지를 체크해주었다.
"""