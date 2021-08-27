import sys


def Bracket(depth, result):
    if depth == N:
        intRe = int(result)
        global mini, maxi

        if mini > intRe:
            mini = intRe
        if maxi < intRe:
            maxi = intRe

        return

    for i in range(10):
        if visit[i]:
            continue

        if depth == 0:
            visit[i] = True
            Bracket(depth+1, result+str(i))
            visit[i] = False
            continue

        if brackets[depth-1] == "<":
            if int(result[depth-1]) < i:
                visit[i] = True
                Bracket(depth+1, result+str(i))
                visit[i] = False
        elif brackets[depth-1] == ">":
            if int(result[depth-1]) > i:
                visit[i] = True
                Bracket(depth+1, result+str(i))
                visit[i] = False


K = int(sys.stdin.readline())
N = K+1
brackets = sys.stdin.readline().split()
visit = [False for _ in range(10)]
mini = 9876543210
maxi = 0
Bracket(0, '')
if len(str(maxi)) != N:
    print('0' + str(maxi))
else:
    print(maxi)
if len(str(mini)) != N:
    print('0' + str(mini))
else:
    print(mini)

