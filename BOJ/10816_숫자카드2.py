N = int(input())
cardList = sorted(list(map(int, input().split())))
cardCount = dict.fromkeys(set(cardList))
for card in cardList:
    if cardCount[card] is not None:
        cardCount[card] += 1
    else:
        cardCount[card] = 1
cardList = sorted(set(cardList))
M = int(input())
mList = list(map(int, input().split()))


def binarySearch(a):
    first = 0
    last = len(cardList) - 1
    mid = int((first + last) / 2)

    while first <= last:
        if cardList[mid] == a:
            return cardCount[cardList[mid]]
        elif cardList[mid] > a:
            last = mid - 1
            mid = int((first + last) / 2)
        else:
            first = mid + 1
            mid = int((first + last) / 2)
    return 0


result = ""
for m in mList:
    result += str(binarySearch(m)) + " "
print(result)

"""
10815 번과 거의 비슷한 이분탐색 문제.
숫자 카드가 중복이라는 점에서 차이점이 있다.
숫자 카드는 각 갯수를 카운팅 한 뒤 중복을 없애버리고 기존과 같이 이분탐색한다.
원하는 값을 찾았을 때 카운팅한 갯수를 출력하고
값을 찾지 못하면 0 을 출력한다.
"""