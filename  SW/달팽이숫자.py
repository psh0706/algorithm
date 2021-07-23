
# -*- coding: utf-8 -*-

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = [[ 0 for _ in range(N) ]for _ in range(N)]
    visit = [[ 0 for _ in range(N) ]for _ in range(N)]
    x,y = 0,0
    num = 1

    arr[x][y] = num
    visit[x][y] = 1
    num += 1

    while num <= (N ** 2):
        #right
        while (y+1) != N and visit[x][y+1] == 0:
            y += 1
            arr[x][y] = num
            visit[x][y] = 1
            num += 1

        #down
        while (x+1) != N and visit[x+1][y] == 0:
            x += 1
            arr[x][y] = num
            visit[x][y] = 1
            num += 1

        #left
        while (y-1) != -1 and visit[x][y-1] == 0:
            y -= 1
            arr[x][y] = num
            visit[x][y] = 1
            num += 1

        #up
        while (x-1) != -1 and visit[x-1][y] == 0:
            x -= 1
            arr[x][y] = num
            visit[x][y] = 1
            num += 1

    print("#"+str(test_case))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=" ")
        print()