T = int(input())
for _ in range(T):

    p = list(input())
    n = int(input())
    characters = "[]"
    arr = ''.join(x for x in input() if x not in characters)
    arr = arr.split(',')
    if '' in arr:
        arr.remove('')

    R = False
    err = False
    front, back = 0, n - 1

    for x in p:
        if x == "R":
            R = not R
        else:
            if front > back:
                err = True
                break
            if R:
                back -= 1
            else:
                front += 1

    if err:
        print("error")
    else:
        answer = ""
        if R:
            for i in range(back, front - 1, -1):
                answer += arr[i] + ","
        else:
            for i in range(front, back + 1):
                answer += arr[i] + ","

        answer = '[' + answer[:-1] + "]"
        print(answer)


"""
R, D 를 모두 연산하는게 아니라
포인터를 숫자 리스트에 두고, R 이면 리버스 flag 를 변환해준다.
D면 리버스 flag 에 따라 front 나 back 포인터를 한칸 이동하는 방식으로 진행했다.
중요한것은 예외처리인데
front 가 back 보다 하나 크다는것은 방금 전 연산으로 배열이 비었다는 것을 의미한다.
배열이 비어있는데 D 연산을 하면 에러처리해주어야한다.
하지만 배열이 비어 있을 때 R 연산을 하는것은 에러가 아니다 << 이거 때문에.. 엄청 틀렸다...
"""