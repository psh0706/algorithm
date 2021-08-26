def lotto(depth, start, result):
    if depth == 6:
        print(result)
        return

    for i in range(start, len(s)):
        lotto(depth+1, i+1, result+s[i]+" ")


while True:
    li = input()

    # 0을 받는 순간 break
    if li == '0':
        break

    # make s
    s = li.split()[1:]

    # 재귀
    lotto(0, 0, "")
    print()
