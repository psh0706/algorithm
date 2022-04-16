import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    age, name = sys.stdin.readline().split(" ")
    arr.append([int(age), name])
arr.sort(key=lambda x: x[0])
answer = ""
for [age, name] in arr:
    answer += str(age) + " " + name
print(answer)

"""
간단한 정렬문제
"""