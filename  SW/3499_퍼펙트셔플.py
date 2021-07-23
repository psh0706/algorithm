T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    ori_deck = input().split()
    ans = []
    mid_index = 0

    if N % 2 == 0:
        mid_index = N // 2
    else:
        mid_index = N // 2+1

    deck1 = ori_deck[0:mid_index]
    deck2 = ori_deck[mid_index:]

    for _ in range(len(deck1)):
        if len(deck2) == 0:
            ans.append(deck1.pop(0))
        else:
            ans.append(deck1.pop(0))
            ans.append(deck2.pop(0))

    print("#" + str(test_case), end=" ")
    for word in ans:
        print(word, end=" ")
    print()