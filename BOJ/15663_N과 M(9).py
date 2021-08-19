def perm(depth, result):
    if depth == M:
        print(result)

    for i in string_dict.keys():
        if string_dict[i] == 0:
            continue
        else:
            string_dict[i] -= 1
            perm(depth+1, result+i+" ")
            string_dict[i] += 1


N, M = map(int, input().split())
integers = [str(i) for i in sorted(map(int, input().split()))]
string_dict = dict.fromkeys(integers)

# 카운팅
for i in integers:
    if not string_dict[i]:
        string_dict[i] = 1
    else:
        string_dict[i] += 1

perm(0, '')

