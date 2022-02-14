class DiceLoc:
    def __init__(self, bot, top, E, W, N, S):
        self.bot = bot
        self.top = top
        self.E = E
        self.W = W
        self.N = N
        self.S = S


def moveDice(loc, op):
    if op == 1:
        # E
        return DiceLoc(loc.E, loc.W, loc.top, loc.bot, loc.N, loc.S)
    elif op == 2:
        # W
        return DiceLoc(loc.W, loc.E, loc.bot, loc.top, loc.N, loc.S)
    elif op == 3:
        # N
        return DiceLoc(loc.N, loc.S, loc.E, loc.W, loc.top, loc.bot)
    else:
        # S
        return DiceLoc(loc.S, loc.N, loc.E, loc.W, loc.bot, loc.top)


def solution():
    r, c, x, y, n = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(r)]
    ops = list(map(int, input().split()))

    delta = [[], [0, 1], [0, -1], [-1, 0], [1, 0]]
    # [[], E, W, N, S]
    # index 0 is not used

    dice = [0 for _ in range(7)]
    # index 0 is not used - for efficiency

    diceLoc = DiceLoc(6, 1, 3, 4, 2, 5)
    # initial dice position

    for op in ops:
        dx = x + delta[op][0]
        dy = y + delta[op][1]
        if 0 <= dx < r and 0 <= dy < c:
            if MAP[x][y] == 0:
                MAP[x][y] = dice[diceLoc.bot]
            else:
                dice[diceLoc.bot] = MAP[x][y]
                MAP[x][y] = 0
            # bottom paste
            diceLoc = moveDice(diceLoc, op)
            x, y = dx, dy
            # move dice
            print(dice[diceLoc.top])
            # top of dice


solution()

"""
1. 주사위를 굴릴 때 마다, 주사위의 바닥, 윗면, 동쪽 면, 서쪽 면, 북쪽 면, 남쪽 면을 계산한다. (move dice)
2. 만약 이동할수 없는 곳으로 이동할 때에는 바닥과의 상호작용이 없어야한다. << 중요
"""
