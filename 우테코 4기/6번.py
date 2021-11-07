def solution(time, plans):
    answer = ''
    lastPlace = ''

    for plan in plans:
        lastPlace = plan[0]
        dptureAdd = plan[1][-2:]
        dptureTime = int(plan[1][:-2])
        arvAdd = plan[2][-2:]
        arvTime = int(plan[2][:-2])

        t = 0

        # 금요일 출발
        if dptureAdd == "AM" and dptureTime < 9.5:
            t += 8.5
        elif (dptureAdd == "AM" and dptureTime > 9.5) or (dptureAdd == "PM" and dptureTime < 6):
            if dptureAdd == "AM":
                t += 12 - dptureTime + 6
            else:
                t += 6 - dptureTime
        else:
            t += 0

        # 월요일 도착
        if arvAdd == "AM" or (arvAdd == "PM" and arvTime < 1):
            t += 0
        elif (arvAdd == "PM" and arvTime > 1) and (arvAdd == "PM" and dptureTime < 6):
            t += arvTime - 1
        else:
            t += 5

        if time < t:
            break
        else:
            time -= t
            answer = lastPlace

    return answer