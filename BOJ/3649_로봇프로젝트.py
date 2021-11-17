import copy

while True:
    try:
        x = int(input()) * 10000000
        n = int(input())
        legoList = [int(input()) for _ in range(n)]

        if n < 2:
            print("danger")
        else:
            legoList.sort()

            flag = False
            maxi = -1
            l1, l2 = 0, 0

            for i in range(n):
                find = x - legoList[i]

                # legoTemp = copy.deepcopy(legoList[i + 1:])

                st, ed = i+1, n - 1

                while ed >= st:
                    mid = int((ed + st) / 2)
                    if find == legoList[mid]:
                        flag = True

                        gap = abs(legoList[i] - legoList[mid])
                        if maxi < gap:
                            maxi = gap
                            l1 = legoList[i]
                            l2 = legoList[mid]
                        break

                    elif find > legoList[mid]:
                        st = mid + 1
                    else:
                        ed = mid - 1

                if flag:
                    break

            if flag:
                print("yes " + str(l1) + " " + str(l2))
            else:
                print("danger")

    except:
        break

"""
정렬 + 이분탐색
copy.deepcopy 때문에 시간초과로 고생했다.
딥카피 쓸 때는 시간에 유의하기..
"""