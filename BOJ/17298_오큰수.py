n = int(input())
arr = list(map(int, input().split(" ")))

stack = []
answer = [-1 for _ in range(n)]

for i in range(n):
    if not stack:
        stack.append([arr[i], i])
        continue

    while True:
        if not stack:
            stack.append([arr[i], i])
            break

        if stack[-1][0] < arr[i]:
            answer[stack[-1][1]] = arr[i]
            stack.pop(-1)
        else:
            stack.append([arr[i], i])
            break

print(' '.join(map(str, answer)))

"""
수열의 최대 크기가 100만 이므로 O(n) 안으로 끝내야하는 문제
그러려면 선형 탐색 한번만에 오큰수를 알아내야하므로 stack 을 이용했다.
핵심은 자신보다 큰 수가 나올 때 까지 stack 에서 대기하는 것
그렇게 되면 stack 은 자연스럽게 큰 수가 밑으로, 작은수가 위로 올라가게 되므로 오큰수를 찾을 수 있다.
"""
