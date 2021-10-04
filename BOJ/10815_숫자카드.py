N = int(input())
cardList = sorted(list(map(int, input().split())))
M = int(input())
mList = list(map(int, input().split()))


def binarySearch(a):
    first = 0
    last = N - 1
    mid = int((first + last) / 2)

    while first <= last:
        if cardList[mid] == a:
            return '1'
        elif cardList[mid] > a:
            last = mid - 1
            mid = int((first + last) / 2)
        else:
            first = mid + 1
            mid = int((first + last) / 2)
    return '0'


result = ""
for m in mList:
    result += binarySearch(m) + " "
print(result)

"""
기초 이분탐색 문제 !
"""