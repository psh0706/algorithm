import copy

R, C = map(int, input().split())
I = [0, 0]
Rs = []
for r in range(R):
    line = list(input())
    for c in range(C):
        if line[c] == 'I':
            I[0] = r
            I[1] = c
        elif line[c] == 'R':
            Rs.append([r, c])
moves = list(map(int, list(input())))
move = [[0, 0], [1, -1], [1, 0], [1, 1], [0, -1],[0, 0], [0, 1], [-1, -1], [-1, 0], [-1, 1]]

MAP = [[0 for _ in range(C)] for _ in range(R)]
for a in Rs:
    MAP[a[0]][a[1]] += 1

cnt = 0
flag = True
for m in moves:
    cnt += 1

    I[0] += move[m][0]
    I[1] += move[m][1]

    if I in Rs:
        flag = False
        print('kraj ' + str(cnt))
        break

    r1, c1 = I[0], I[1]
    for i in range(len(Rs)):
        r, c = Rs[i][0], Rs[i][1]
        MAP[r][c] -= 1
        minR, minC = 0, 0
        mini = 99999
        for j in range(1, len(move)):
            r2 = r + move[j][0]
            c2 = c + move[j][1]
            gap = abs(r1 - r2) + abs(c1 - c2)
            if mini > gap:
                minR, minC = r2, c2
                mini = gap
        MAP[minR][minC] += 1
        Rs[i][0] = minR
        Rs[i][1] = minC

    if I in Rs:
        flag = False
        print('kraj ' + str(cnt))
        break

    for i in range(R):
        for j in range(C):
            if MAP[i][j] >= 2:
                for _ in range(MAP[i][j]):
                    Rs.remove([i, j])
                MAP[i][j] = 0

if flag:
    MAP = [['.' for _ in range(C)] for _ in range(R)]
    MAP[I[0]][I[1]] = 'I'
    for R in Rs:
        MAP[R[0]][R[1]] = 'R'

    for l in MAP:
        line = ""
        for x in l:
            line += x
        print(line)


"""
구현문제 미친 아두이노
아두이노끼리 겹치면 폭발하는 부분에서 .count 내장함수를 사용했다가
시간초과 폭탄을 맞았다.. (원인을 못찾아서 ㅠㅠ)
이동할 때 마다 카운팅하는 방법으로 바꾸고 성공 ..!
"""