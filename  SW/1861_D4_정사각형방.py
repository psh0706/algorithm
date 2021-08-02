T = int(input())

for test_case in range(1, T + 1):

    N = int(input())
    roomList = [[int(x) for x in input().split()] for __ in range(N)]
    max = 0
    final_x, final_y = 0, 0

    for i in range(N):
        for j in range(N):
            sum = 0
            x = i
            y = j
            while True:

                if (x - 1 != -1) and roomList[x][y]+1 == roomList[x - 1][y]:
                    x -= 1
                    sum += 1
                elif (x + 1 != N) and roomList[x][y]+1 == roomList[x + 1][y]:
                    x += 1
                    sum += 1
                elif (y - 1 != -1) and roomList[x][y]+1 == roomList[x][y - 1]:
                    y -= 1
                    sum += 1
                elif (y + 1 != N) and roomList[x][y]+1 == roomList[x][y + 1]:
                    y += 1
                    sum += 1
                else:
                    break
            if max < sum:
                max = sum
                final_x = i
                final_y = j
            elif max == sum:
                if roomList[i][j] < roomList[final_x][final_y]:
                    final_x = i
                    final_y = j
                else:
                    pass
            else:
                pass

    print("#" + str(test_case) + " " + str(roomList[final_x][final_y]) + " " + str(max+1))
