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
11054 번의 가장 긴 증가하는 부분수열보다 n의 범위가 100만으로 커지고,
부분수열의 길이가 아닌 부분수열 자체를 구하는 문제이다.

nlog(n) 의 시간복잡도를 가지도록 이분 탐색을 사용한 LIS (최장 증가수열) 알고리즘을 사용 했기 때문에
1000000*5*log10 = 1000000 * 5 = 5000000 로 시간초과 문제가 없다.
"""
