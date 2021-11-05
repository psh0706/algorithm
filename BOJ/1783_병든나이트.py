h, w = map(int, input().split())

if h == 1:
    print(1)
elif h == 2:
    if 1 <= w <= 2:
        print(1)
    elif 3 <= w <= 4:
        print(2)
    elif 5 <= w <= 6:
        print(3)
    else:
        print(4)
else:
    if w < 4:
        print(w)
    elif 4 <= w <= 6:
        print(4)
    else:
        print(w-4+2)


"""
그리디 구현 문제
세로와 가로의 범위를 지정하기만 하면 된다.
"""