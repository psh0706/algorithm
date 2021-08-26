def encoding(depth, start, result):
    if depth == L:
        temp = list(result)
        vSum = 0
        cSum = 0
        for t in temp:
            if ('a' == t) or ('i' == t) or ('u' == t) or ('e' == t) or ('o' == t):
                vSum += 1
            else:
                cSum += 1

        if vSum >= 1 and cSum >= 2:
            print(result)
        return

    for i in range(start, len(arr)):
        encoding(depth+1, i+1, result+arr[i])


L, C = map(int, input().split())
arr = list(input().split())
arr = sorted(arr)
encoding(0, 0, '')



