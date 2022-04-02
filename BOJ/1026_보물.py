n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(key=lambda x: x)
b.sort(key=lambda x: -x)

answer = 0
for i in range(n):
    answer += a[i]*b[i]

print(answer)

"""
b의 큰수에 a의 작은수를 곱하고, a의 작은수에 b의 큰 수를 곱할 때 가장 큰 작은 수를 찾을 수 있다.
a 배열을 마음대로 재배열 할 수 있고, 배열 순서를 출력 하는 것이 아니라 결과 값을 출력하는것이기 때문에
그냥 마음대로 정렬해서 사용해도 된다.

a를 오름차순 정렬, b를 내림차순 정렬해서 순서대로 곱한것을 누적합 하면 된다.
"""