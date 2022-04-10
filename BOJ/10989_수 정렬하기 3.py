import sys

n = int(input())
count = [0 for _ in range(10001)]

for _ in range(n):
    num = int(sys.stdin.readline())
    count[num] += 1

string = ""
for i in range(1, 10001):
    if count[i] > 0:
        i_str = str(i)
        for _ in range(count[i]):
            sys.stdout.write(i_str+"\n")

"""
1억번 입력이 들어오기때문에 전부 저장하면 메모리 초과 -> 카운팅 하는 방식을 이용해야한다.
입력이 나누어져서 개행되어 들어오기 때문에 input()을 쓰면 메모리 초과
출력을 print()로 하는 것 보다 sys.stdout.write()를 사용해야한다.
"""