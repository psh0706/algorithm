def overPerm(depth, result):
    if depth == M:
        print(result)
        return

    for i in range(0, N):
        # 별도의 리스트에 넣고 빼지 않고 매개변수로 넘길 때 문자열로 붙혀서 보내고 버림.
        overPerm(depth+1, result+string[i])


N, M = map(int, input().split())
# 문자열 배열로 접근
string = [str(i)+' ' for i in sorted(map(int, input().split()))]

overPerm(0, '')
