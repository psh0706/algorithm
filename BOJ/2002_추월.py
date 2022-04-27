n = int(input())
IN = [input() for _ in range(n)]
OUT = {input(): i for i in range(n)}
stack = []

for i in range(n):
    if stack and stack[-1] > OUT[IN[i]]:
        continue
    else:
        stack.append(OUT[IN[i]])

print(n - len(stack))

"""
들어간 순서와 나온 순서를 비교한다.
나온 순서를 들어간 순서에 맵핑하고, 
맨 처음 들어간 차를 기준으로하는 증가하는 부분 수열을 찾으면 된다.
stack 을 이용해 오름차순을 유지하는 방법을 사용해 풀어보았다.
"""