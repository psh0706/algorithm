n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]

for point in points:
    gap = point[1] - point[0]
    lightYear = 1
    operations = 0

    while True:
        if gap <= 0:
            break
        if gap <= lightYear:
            operations += 1
            break
        gap -= (2 * lightYear)
        operations += 2
        lightYear += 1

    print(operations)


"""
공간이동장치가 이전 작동시기에 k광년을 이동하였을 때는 k-1 , k 혹은 k+1 광년만을 다시 이동할 수 있고
도착시 1광년으로 도착해야하기때문에

(출발)1 .... 1(도착) 
의 모양이된다.

기본적으로 최소 작동수를 구하는것이기 때문에, 한번에 크게크게 움직이는게 이득이다.
1광년이 되기 위해 가장 크게 이동할수 있는 광년수는 2광년이다. 따라서 다음과 같은 모양이된다.
(출발)1 2 .... 2 1(도착)

그다음은  
(출발)1 2 3 .... 3 2 1(도착)
이 될 것이다.

이것은 k광년이 공간의 gap 차이에서 2k 광년씩 빠지는 꼴이 되는데
그러다 어느 순간 gap보다 이동할 광년 수가 커지는 상황이온다.

ex)
case1)
gap = 0~19
1 2 3 ... 3 2 1
k = 4 이고 (2k = 8) 
남은 gap은 7이기 때문에.
7-8 이동 불가.

case2)
gap = 0~15
1 2 3 ... 3 2 1
k = 4 이고 (2k = 8) 
남은 gap은 3이기 때문에.
3-8 이동 불가.

case3)
gap = 0~16
1 2 3 ... 3 2 1
k = 4 이고 (2k = 8) 
남은 gap은 3이기 때문에.
4-8 이동 불가.


이때 남은 gap이 k광년보다 작거나 같다면, 그 수만큼을 해당하는 곳에 넣어주면 된다.
-> case1 은 남은 갭이 7이고 k가 4 이므로 1 2 3 (4) (3) 3 2 1 순서로 이동하면 된다.
-> case2 은 남은 갭이 4이고 k가 4 이므로 1 2 3 (4) 3 2 1 순서로 이동하면 된다.
-> case3 일 경우 남은 갭이 3이고 k가 4 이므로 1 2 3 (3) 3 2 1 순서로 이동하면 된다.
"""