from collections import deque


def solution(board, skill):
    answer = 0
    delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    R = len(board)
    C = len(board[0])

    for s in skill:
        t = s[0]
        r1 = s[1]
        c1 = s[2]
        r2 = s[3]
        c2 = s[4]
        degree = s[5]
        visit = [[False for _ in range(C)] for _ in range(R)]

        q = deque([[r1, c1]])
        if t == 1:
            board[r1][c1] -= degree
        else:
            board[r1][c1] += degree
        visit[r1][c1] = True

        while len(q) != 0:
            n = q.popleft()

            for d in delta:
                dx = n[0] + d[0]
                dy = n[1] + d[1]

                if r1 <= dx <= r2 and c1 <= dy <= c2 and not visit[dx][dy]:
                    visit[dx][dy] = True
                    q.append([dx, dy])
                    if t == 1:
                        board[dx][dy] -= degree
                    else:
                        board[dx][dy] += degree

    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                answer += 1


    return answer


solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],
         [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])