import sys

n = int(sys.stdin.readline())
top_list = list(map(int, sys.stdin.readline().split()))

answer_list = ['0']*n
stack = list()


for i in range(n-1,-1,-1):

    stack.append(i)

    if len(stack) < 1:
        continue

    j = len(stack) - 2
    while top_list[stack[-1]] > top_list[stack[j]]:
        answer_list[stack[j]] = str(i+1)
        del stack[j]
        j = j - 1
        if j < 0:
            break


print(' '.join(answer_list))
