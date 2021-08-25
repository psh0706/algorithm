def quardTree(hx, hy, m):
    if m == 1:
        hx = int(hx)
        hy = int(hy)
        if video[hx][hy] == '1':
            return '1'
        else:
            return '0'

    temp = ""
    # 1사분면
    temp += quardTree(hx - (m / 4), hy - (m / 4), m / 2)
    # 2사분면
    temp += quardTree(hx - (m / 4), hy + (m / 4), m / 2)
    # 3사분면
    temp += quardTree(hx + (m / 4), hy - (m / 4), m / 2)
    # 4사분면
    temp += quardTree(hx + (m / 4), hy + (m / 4), m / 2)

    acc = 0
    for i in list(temp[-4:]):
        if i == '(' or i == ')':
            return "(" + temp + ")"
        else:
            acc += int(i)
    if acc == 4 or acc == 0:
        return temp[:-3]
    else:
        return "(" + temp + ")"


N = int(input())
video = [[x for x in input()] for _ in range(N)]
print(quardTree(N / 2, N / 2, N))
