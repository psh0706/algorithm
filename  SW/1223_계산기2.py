test_result = ""

for i in range(10):
    N = int(input())
    arr = list(input())
    calc_stack = list()
    operator_stack = list()

    #후위계산식 만들기
    for stuff in arr:
        if stuff == "+":
            if len(operator_stack) == 0:
                pass
            else:
                while True:
                    if len(operator_stack) == 0: break
                    calc_stack.append(operator_stack.pop())
            operator_stack.append(stuff)
        elif stuff == "*":
            if len(operator_stack) == 0:
                pass
            else:
                while len(operator_stack) == 0:
                    if operator_stack[-1] == "+":
                        operator_stack.append(stuff)
                        break
                    else:
                        calc_stack.append(operator_stack.pop())
            operator_stack.append(stuff)
        else:
            calc_stack.append(int(stuff))

    if len(operator_stack) == 0 : pass
    else:
        for _ in range(len(operator_stack)):
            calc_stack.append(operator_stack.pop())

    #계산
    result_stack = list()
    for item in calc_stack:
        if item == "*":
            val1 = result_stack.pop()
            val2 = result_stack.pop()
            result_stack.append(val1*val2)
        elif item == "+":
            val1 = result_stack.pop()
            val2 = result_stack.pop()
            result_stack.append(val1 + val2)
        else:
            result_stack.append(item)

    test_result += "#"+str(i+1)+" "+str(result_stack.pop())+'\n'

print(test_result)