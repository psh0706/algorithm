n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: [x[0], x[1]])
for i in range(n):
    print(str(arr[i][0]) + " " + str(arr[i][1]))

"""
정렬 기준이 2개일때의 정렬
람다 표현식 이용
"""