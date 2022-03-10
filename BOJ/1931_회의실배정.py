n = int(input())
meets = [list(map(int, input().split())) for _ in range(n)]
meets.sort(key=lambda x: (x[1], x[0]))
nowMeet = meets[0]
cnt = 1

for i in range(1, n):
    if nowMeet[1] <= meets[i][0]:
        nowMeet = meets[i]
        cnt += 1

print(cnt)


"""
끝나는 시간만 정렬 -> WA 
반례 : 
3
1 3
8 8
4 8
답: 3
오답: 2

시작시간, 끝나는시간 함께 정렬 -> AC
"""