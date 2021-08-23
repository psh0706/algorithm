def zCount(hx, hy, m, acm):

    if m == 1:
        print(int(acm))
        return

    if r <= hx-1 and c <= hy-1:
        zCount(hx-(m/4), hy-(m/4), m/2, acm)
        return
    else:
        acm += (m/2)**2
    if r <= hx-1 and c >= hy:
        zCount(hx-(m/4), hy+(m/4), m/2, acm)
        return
    else:
        acm += (m/2)**2
    if r >= hx and c <= hy-1:
        zCount(hx+(m/4), hy-(m/4), m/2, acm)
        return
    else:
        acm += (m/2)**2
    if r >= hx and c >= hy:
        zCount(hx+(m/4), hy+(m/4), m/2, acm)
        return


N, r, c = map(int, input().split())
M = 1 << N

zCount(M/2, M/2, M, 0)
