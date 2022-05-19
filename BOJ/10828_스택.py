from collections import deque
import sys

n = int(input())
ops = [list(sys.stdin.readline().replace("\n", "").split(" ")) for _ in range(n)]
stack = deque()

for op in ops:
    if op[0] == "push":
        stack.append(int(op[1]))
    elif op[0] == "pop":
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif op[0] == "top":
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
    elif op[0] == "size":
        print(len(stack))
    else:
        if len(stack) > 0:
            print(0)
        else:
            print(1)

"""
deque 를 이용해 풀어본 stack 구현 문제

파이썬의 일반 list 는 순차 list 로 구현되어 있어
삽입/삭제시 뒤 요소들을 한칸씩 밀어내기 때문에 
삽입 삭제가 많은 연산을 할 때에 성능이 좋지 않을 수 있다.

하지만 deque 같은 경우 연결 list 로 구현되어 있기 때문에 
삽입 삭제가 많은 연산에서도 좋은 성능을 낸다. 

사실 스택의 경우에는 끝에서만 삽입/삭제가 이루어지기 때문에 
둘 사이에 큰 성능차는 없으나.. 혹시나 해서!
"""

