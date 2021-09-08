import sys
from collections import deque


def left(integer):
    temp = int(integer / 1000)
    return (integer % 1000)*10 + temp


def right(integer):
    temp = int(integer % 10)
    return int(integer / 10) + temp*1000


def bfs(A, B):
    q = deque()
    visit = [False] * 10000

    visit[A] = True
    q.append([A, ""])

    while q:

        num, operation = q.popleft()

        if num == B:
            return operation

        L = left(num)
        if not visit[left(num)]:
            visit[L] = True
            q.append([L, operation + "L"])

        R = right(num)
        if not visit[R]:
            visit[R] = True
            q.append([R, operation + "R"])

        D = (num * 2) % 10000
        if not visit[D]:
            visit[D] = True
            q.append([D, operation + "D"])

        S = 9999 if num == 0 else num - 1
        if not visit[S]:
            visit[S] = True
            q.append([S, operation + "S"])


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        start, end = map(int, sys.stdin.readline().split())
        print(bfs(start, end))


# 진짜 진짜 진짜 오래걸린문제.. 문제 이해부터 로직 구현까지 삼십분도 안걸렸는데 자꾸만 시간초과가 뜨는 것임
# 진짜 도대체 왜 때문인지 몰라서 거의 4시간을 헤맸다
# 결국 이건 내가 해결할 수 없는 문제라고 생각하고 다른 분이 짠 코드를 열람함
# 나는 시간초과가 문자열연산 탓인줄 알고 별의 별 짓을 다해 문자열 연산 수를 줄였는데
# 그분은 너무 편안하고 이지하게 코드를 짜신것이다..? 근데 통과를 하셨다고 한다...?
# 다른점은 딱 두개 있었음
# 1. 리스트가 아닌 데크를 사용함
# 2. 메인 모듈을 사용함 (문제가 테케를 받아서 돌리는거라 킹리적 갓심 작용)
# 우선 둘 다 고쳐서 제출했고 결과는 통과.
# 원인을 찾아보니 "2. 메인모듈 사용" 은 문제가 아니였다 ㅋ
# 바로바로... 리스트를 넣고 빼는 연산이 많아졌을 때의 문제였는데..
# 보통 pop, push 연산이 많을 경우 리스트보다 데크가 성능이 탁월하다는 것이다
# 이렇게 한가지를 더 배워간다... 앞으로 데크를 애용해야겠다 하하..
