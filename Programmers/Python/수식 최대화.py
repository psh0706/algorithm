import re
import itertools


def calc(op, a, b):
    if op == '-':
        return a - b
    elif op == '+':
        return a + b
    elif op == '*':
        return a * b
    else:
        return


def solution(expression):
    answer = 0

    # 기본 셋팅
    priority = list(itertools.permutations(['+', '-', '*']))
    exp = re.split('([-|+|*])', expression)

    # 우선순위 별 계산 결과로 최대값 파악
    for opList in priority:
        tempExp = [item for item in exp]
        for op in opList:
            stack = []
            i = 0
            while i < len(tempExp):
                if tempExp[i] == op:
                    stack.append(calc(op, int(stack.pop(-1)), int(tempExp[i + 1])))
                    i += 2
                else:
                    stack.append(tempExp[i])
                    i += 1

            if len(stack) == 1:
                if answer == 0:
                    answer = abs(stack[0])
                answer = max(answer, abs(stack[0]))
            else:
                tempExp = stack

    return answer


solution("100-200*300-500+20")

"""
연산자의 우선순위롤 permutations 를 통해 만들어주고
우선순위 별 연산 결과 중 최대값을 찾아냈다.
연산에는 stack 을 활용해 해당하는 연산자가 나올 때만 계산하도록 했다.
"""