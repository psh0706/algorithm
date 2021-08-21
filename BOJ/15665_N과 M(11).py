def comb(depth, result):
    if depth == M:
        print(result)
        return

    for i in string_list:
        comb(depth+1, result+i+" ")


N, M = map(int, input().split())
integers = [str(i) for i in sorted(map(int, input().split()))]
string_list = list(dict.fromkeys(integers))

comb(0, "")
