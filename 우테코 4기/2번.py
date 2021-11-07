def solution(log):
    answer = ''

    acc = 0

    for i in range(0, len(log), 2):
        H1, M1 = map(int, log[i].split(":"))
        H2, M2 = map(int, log[i + 1].split(":"))

        if H1 > H2:
            H2 += 24

        if M2 > M1:
            M2 += 60
            H2 -= 1

        minute = (H2 - H1) * 60 + (M2 - M1)

        if minute < 5:
            minute = 0
        elif minute > 105:
            minute = 105

        acc += minute

    H = acc // 60
    M = acc % 60

    if H > 9:
        H = str(H)
    else:
        if H == 0:
            H = "00"
        else:
            H = "0" + str(H)

    if M > 9:
        M = str(M)
    else:
        if M == 0:
            M = "00"
        else:
            M = "0" + str(M)

    answer = H + ":" + M

    return answer