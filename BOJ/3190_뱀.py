def rotate(C, d):
    if C == "D":
        return [d[1], -d[0]]
    elif C == "L":
        return [-d[1], d[0]]
    return False


def solution():
    cnt = 0
    n = int(input())
    board = [[0 for _ in range(n)] for _ in range(n)]
    snake = [[0, 0]]
    d = [0, 1]
    board[0][0] = 1

    for _ in range(int(input())):
        x, y = map(int, input().split())
        board[x - 1][y - 1] = 2

    L = int(input())
    ops = [input().split() for _ in range(L)] + [[101, 'D']]
    for l in range(L+1):
        X, C = int(ops[l][0]) - cnt, ops[l][1]

        for _ in range(int(X)):
            cnt += 1
            dx = snake[0][0] + d[0]
            dy = snake[0][1] + d[1]

            if 0 > dx or dx >= n or 0 > dy or dy >= n or board[dx][dy] == 1:
                return cnt

            if board[dx][dy] == 2:
                board[dx][dy] = 1
                snake.insert(0, [dx, dy])
            elif board[dx][dy] == 0:
                board[dx][dy] = 1
                snake.insert(0, [dx, dy])
                board[snake[-1][0]][snake[-1][1]] = 0
                snake.pop()

        d = rotate(C, d)

    return cnt


print(solution())


"""
빡구현 문제 뱀
회전하는 함수를 별도로 두었고, 
snake 리스트를 두어서 snake[0] = 뱀의 머리, snake[-1] = 뱀의 꼬리 라고 생각하고 풀었다.
중요한것은 명령어
8 D
10 D
11 D
13 L
+8초 후 오른쪽 회전
+10초 후 오른쪽 회전
+11초 후 오른쪽 회전
+13초 후 왼쪽 회전 이 아니라

+8초 후 오른쪽 회전
+2초 후 오른쪽 회전
+1초 후 오른쪽 회전
+2초 후 왼쪽 회전 이다.
"""