import math


def solution(fees, records):
    answer = []
    basicTime = fees[0]
    basicFee = fees[1]
    unitTime = fees[2]
    unitFee = fees[3]

    info = dict()

    for r in records:
        time, number, io = r.split()

        h, m = map(int, time.split(":"))
        minutes = (h * 60) + m

        if number in info:
            info[number].append([io, minutes])
        else:
            info[number] = [[io, minutes]]

    timeInfo, feeInfo = dict.fromkeys(info), dict.fromkeys(info)

    for key in info:
        car = info[key]
        if len(car) % 2 == 1:
            car.append(['OUT', 1439])

        for i in range(0, len(car), 2):
            if timeInfo[key]:
                timeInfo[key] += car[i + 1][1] - car[i][1]
            else:
                timeInfo[key] = car[i + 1][1] - car[i][1]

    for key in timeInfo:
        time = timeInfo[key]
        fee = 0
        if time >= basicTime:
            fee = basicFee + math.ceil((time - basicTime)/unitTime) * unitFee
        else:
            fee = basicFee

        feeInfo[key] = fee

    for key, value in sorted(feeInfo.items()):
        answer.append(value)

    return answer


solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT",
                               "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
                               "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])