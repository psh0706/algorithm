n = int(input())
p = list(map(int, input().split()))
p.sort()

answer = 0
temp = 0
for i in range(n):
    temp += p[i]
    answer += temp

print(answer)

"""
각 사람들에게 걸리는 인출 시간 p는 언제나 같다 (순서가 바뀌어도 항상 같다)
따라서 전체적인 인출 시간을 줄이기 위해서는 인출을 시작하기 까지 걸리는 시간을 최소화 해야한다.
=> 인출 순서를 인출 시간 p가 작은 순서대로 정렬해야한다.
"""