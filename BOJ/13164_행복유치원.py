n, k = map(int, input().split())
children = list(map(int, input().split()))

diff = []
for i in range(1, n):
    d = children[i]-children[i-1]
    diff.append(d)

diff.sort(reverse=True)

print(sum(diff[k-1:]))

"""
pop 연산 때문에 시간초과 
-> 파이썬의 list 구조가 linked list 인지 array list 인지 확인할 필요가 있다.
array List 는 삽입/삭제시 시간복잡도가 최대 n 이므로 주의해야한다.
"""