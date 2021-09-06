i = 0
year = 0
flag = True
E, S, M = map(int, input().split())


def countYear(depth):
    global i, year, flag

    if depth == 'S':
        while flag:
            year = i*28+S
            countYear('M')
            i += 1

    if depth == 'M':
        restS = year % 19
        if restS == 0:
            restS = 19

        if M == restS:
            countYear('E')
        return

    if depth == 'E':
        restM = year % 15
        if restM == 0:
            restM = 15

        if E == restM:
            print(year)
            flag = False
        return


if E == 1 and S == 1 and M == 1:
    print(1)
else:
    countYear('S')
