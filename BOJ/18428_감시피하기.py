N = int(input())
flag = False
T = []
S = []
O = []
MAP = []


def isCatch(t, dic):
    if dic == "u":
        s = dict({'x': -1, 'y': -1})
        o = dict({'x': -1, 'y': -1})
        for item in S:
            if item['y'] == t['y'] and item['x'] < t['x']:
                if item['x'] > s['x']:
                    s = item
        for item in O:
            if item['y'] == t['y'] and item['x'] < t['x']:
                if item['x'] > o['x']:
                    o = item

        if (s['x'] == -1 and s['y'] == -1) or s['x'] < o['x'] < t['x']:
            return True
        else:
            return False
    elif dic == "d":
        s = dict({'x': N, 'y': N})
        o = dict({'x': N, 'y': N})
        for item in S:
            if item['y'] == t['y'] and item['x'] > t['x']:
                if item['x'] < s['x']:
                    s = item
        for item in O:
            if item['y'] == t['y'] and item['x'] > t['x']:
                if item['x'] < o['x']:
                    o = item

        if (s['x'] == N and s['y'] == N) or s['x'] > o['x'] > t['x']:
            return True
        else:
            return False
    elif dic == "l":
        s = dict({'x': -1, 'y': -1})
        o = dict({'x': -1, 'y': -1})
        for item in S:
            if item['x'] == t['x'] and item['y'] < t['y']:
                if item['y'] > s['y']:
                    s = item
        for item in O:
            if item['x'] == t['x'] and item['y'] < t['y']:
                if item['y'] > o['y']:
                    o = item

        if (s['x'] == -1 and s['y'] == -1) or s['y'] < o['y'] < t['y']:
            return True
        else:
            return False
    else:
        s = dict({'x': N, 'y': N})
        o = dict({'x': N, 'y': N})
        for item in S:
            if item['x'] == t['x'] and item['y'] > t['y']:
                if item['y'] < s['y']:
                    s = item
        for item in O:
            if item['x'] == t['x'] and item['y'] > t['y']:
                if item['y'] < o['y']:
                    o = item

        if (s['x'] == N and s['y'] == N) or s['y'] > o['y'] > t['y']:
            return True
        else:
            return False


def recur(depth):
    global flag
    if depth == 3:
        for t in T:
            if not isCatch(t, "u") or not isCatch(t, "d") or not isCatch(t, "l") or not isCatch(t, "r"):
                return
        flag = True
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
else:
    print("YES")


"""
재귀 + 구현 문제
Object 를 재귀로 3개 배치해주고 
선생님의 시야에 학생이 보이는지를 체크해주었다.
+ 오류 수정 완료!
"""