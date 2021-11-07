def solution(arr):
    answer = [0, 0, 0]

    countNum = [0, 0, 0]

    for i in range(1, 4):
        countNum[i - 1] = arr.count(i)
    maxi = max(countNum)

    for i in range(3):
        answer[i] = maxi - countNum[i]

    return answer
