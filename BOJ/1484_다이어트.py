G = int(input())

left, right = 1, 2
result = ''

while True:
    gap = (right*right) - (left*left)

    if gap == G:
        result += str(right) + "\n"

    if gap <= G:
        right += 1
    else:
        if left + 1 == right:
            break
        left += 1

if result == '':
    print(-1)
else:
    print(result)


"""
right^2 - left^2 = G 인 right 값을 찾는 문제 (투포인터)
각 제곱의 차이가 (gap) 

gap <= G : right + 1 하여 gap 을 키운다.
gap > G : left + 1 하여 gap 을 좁힌다.

gap == G 일 때의 right 값을 result 에 저장했다가 한번에 출력
"""