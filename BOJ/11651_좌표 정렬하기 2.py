import sys

n = int(input())
arr = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    arr.append([x, y])

arr.sort(key=lambda item: [item[1], item[0]])
answer = ''
for i in range(n):
    sys.stdout.write(str(arr[i][0])+" "+str(arr[i][1])+"\n")

"""
간단한 정렬 문제
"""

