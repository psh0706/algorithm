N, M = map(int, input().split())
bundle = 1000
ea = 1000

for _ in range(M):
    b, e = map(int, input().split())
    bundle = min(bundle, b)
    ea = min(ea, e)

answer = min(N*ea, int(N/6)*bundle + (N%6)*ea, int(N/6 + 1)*bundle)
print(answer)

"""
낱개 최저가, 번들 최저가를 설정
1. 낱개로만 N개를 사는 경우
2. 번들로 N/6개를 사고, 나머지를 낱개로 사는 경우
3. 그냥 번들로 N/6 + 1 개를 사는경우

세 경우 중 가장 가격이 싼 경우를 선택하면 된다.
"""