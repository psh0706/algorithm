s, P = map(int, input().split())
S = list(input())
minA, minC, minG, minT = map(int, input().split())
DNA = {
    'A': 0,
    'C': 0,
    'G': 0,
    'T': 0
}
for p in range(P):
    DNA[S[p]] += 1

left, right = 0, P - 1
cnt = 0
while True:
    if DNA['A'] >= minA and DNA['C'] >= minC and DNA['G'] >= minG and DNA['T'] >= minT:
        cnt += 1
    if right + 1 == s:
        break
    else:
        DNA[S[left]] -= 1
        DNA[S[right + 1]] += 1
        left += 1
        right += 1

print(cnt)

"""
슬라이딩 윈도우 문제
구간을 옮기며 양쪽 끝을 넣고 빼는 방식이다.
조건의 기준이 되는 A,C,G,T 문자열의 갯수 (최소 개수) 를 받아놓고 시작한다.
갯수는 해시맵으로 관리하는데 한 턴 마다 right 포인터에 해당하는 문자열은 더하고 left 포인터에 해당하는 문자열은 뺀다.
조건에 맞으면 카운팅하는 방식으로 진행한다.
"""