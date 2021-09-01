import sys


N = int(sys.stdin.readline())
arr = list(range(1, N+1))


def nextPermutation():

    i = len(arr)-1
    while i > 0 and arr[i-1] >= arr[i]:
        i -= 1
    if i == 0:
        return False

    j = len(arr) - 1
    while arr[i-1] >= arr[j]:
        j -= 1

    temp = arr[j]
    arr[j] = arr[i-1]
    arr[i-1] = temp

    j = len(arr)-1

    while i < j:
        temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp
        i += 1
        j -= 1

    return True


print(" ".join(map(str, arr)))
while nextPermutation():
    print(" ".join(map(str, arr)))
