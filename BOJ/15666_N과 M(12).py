def comb(depth, start, result):
    if depth == M:
        print(result)
        return

    for i in range(start, len(string_list)):
        comb(depth+1, i, result+string_list[i]+" ")


N, M = map(int, input().split())
integers = [str(i) for i in sorted(map(int, input().split()))]
string_list = list(dict.fromkeys(integers))

comb(0, 0, "")
