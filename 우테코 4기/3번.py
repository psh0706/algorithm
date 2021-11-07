def solution(ings, menu, sell):
    answer = 0

    ingsDict = dict()

    for ing in ings:
        ingName, ingPrice = ing.split()
        ingPrice = int(ingPrice)
        ingsDict[ingName] = ingPrice

    margin = dict()
    for m in menu:
        menuName, ingList, menuPrice = m.split()
        menuPrice = int(menuPrice)

        cost = 0
        for i in ingList:
            cost += ingsDict[i]

        margin[menuName] = menuPrice - cost

    for s in sell:
        menuName, sellCount = s.split()
        sellCount = int(sellCount)

        answer += margin[menuName] * sellCount

    return answer