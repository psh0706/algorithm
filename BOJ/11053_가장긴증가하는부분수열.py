def BinarySearch(array, x):
    left = 0
    right = len(array)-1

    while left <= right:
        mid = (left+right)//2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return left


n = int(input())
li = list(map(int, input().split()))
temp = [li[0]]

for i in range(1, n):
    if li[i] > temp[-1]:
        temp.append(li[i])
    else:
        idx = BinarySearch(temp, li[i])
        temp[idx] = li[i]

print(len(temp))


"""
nlog(n) 의 시간복잡도를 가지도록 이분 탐색을 사용한 LIS (최장 증가수열) 문제!
"""
