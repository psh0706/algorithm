def divide(depth, s, result):
    if depth == half:
        global sub_level
        start = result
        link = [x for x in range(N) if x not in start]
        accS = 0
        accL = 0
        for i in range(half - 1):
            for j in range(i + 1, half):
                accS += S[start[i]][start[j]] + S[start[j]][start[i]]
                accL += S[link[i]][link[j]] + S[link[j]][link[i]]
        sub = abs(accS-accL)
        if sub_level > sub:
            sub_level = sub
        return

    for i in range(s, N):
        result.append(i)
        divide(depth + 1, i + 1, result)
        result.pop()


N = int(input())
half = int(N/2)
S = [list(map(int, input().split())) for _ in range(N)]
sub_level = 99999
divide(0, 0, [])
print(sub_level)
