from itertools import product


def solution():
    string = input()
    length = len(string)
    num = int(string)
    m = int(input())
    MIN = abs(num - 100)

    if m == 0:
        return min(MIN, len(string))

    btn = [str(i) for i in range(10)]
    for broken in input().split():
        btn.remove(broken)

    start, end = length, length + 2
    if length > 1:
        start = length - 1

    for i in range(start, end):
        for li in product(btn, repeat=i):
            press = int(''.join(li))
            MIN = min(MIN, abs(press - num) + len(str(press)))

    return MIN


print(solution())

"""
언듯보면 그리디나 구현쪽 문제 같지만 완전탐색 문제

누를수 있는 버튼으로 만든 모든 번호에서 정답 번호를 찾아가는 경우 vs 100번에서 위아래로만 정답 번호를 찾아가는 경우

itertools 라이브러리를 이용해 주어진 버튼들로 만들 수 있는 버튼의 경우를 (중복순열)로 만들어주었다.
그런데 주어진 번호의 자리수만큼만 찾으면 안되고, 한 자리 작은경우, 한 자리 큰 경우까지 생각해주어야한다.
ex) 반례
1000
2
1 0
-> 999 + up 으로 총 4번이 답이지만
-> 4자리 중복 순열만을 만들 경우 900번이 답이다.
"""