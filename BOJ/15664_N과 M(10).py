def comb(depth, start, result):
    if depth == M:
        print(result)
        return

    for i in range(start,len(string_list)):
        if cnt_list[i] == 0:
            continue
        else:
            cnt_list[i] -= 1
            comb(depth+1, i, result+string_list[i]+" ")
            cnt_list[i] += 1


N, M = map(int, input().split())
integers = [str(i) for i in sorted(map(int, input().split()))]
string_list = list(dict.fromkeys(integers))
cnt_list = [0 for _ in string_list]

# 카운팅
for i in integers:
    cnt_list[string_list.index(i)] += 1

comb(0, 0, '')
