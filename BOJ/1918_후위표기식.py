import sys
from string import ascii_uppercase
from collections import deque
opList = ['+', '-', '*', '/']
in_order = list(sys.stdin.readline())

result = ''
operator = deque()

for e in in_order:
    if e == '(':
        operator.append(e)
    elif e in ascii_uppercase:
        result += e
    elif e in opList:
        if e == '*' or e == '/':
            while len(operator) != 0:
                if operator[-1] == '*' or operator[-1] == '/':
                    result += operator.pop()
                else:
                    break
            operator.append(e)
        elif e == '+' or e == '-':
            while len(operator) != 0:
                if operator[-1] != "(":
                    result += operator.pop()
                else:
                    break
            operator.append(e)
    elif e == ')':
        while True:
            op = operator.pop()
            if op == '(':
                break
            result += op

while operator:
    result += operator.pop()

print(result)

"""
inorder > postorder 변경 문제
앞쪽부터 차례대로 문자는 문자열에 그대로 추가하고, 괄호나 연산자는 스택에 추가한다.
연산자 간의 우선순위가 중요한데, 연산자를 만났을 때 스택의 top이 본인보다 작은게 나올 때 까지 pop하여 문자열에 추가한다.
우선순위는 ( << +, - << *, / 라고 볼 수 있다.
"""