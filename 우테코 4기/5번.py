def solution(rows, columns):
    answer = [[0 for _ in range(columns)] for _ in range(rows)]
    zeros = rows * columns

    if rows == columns:
        r, c = 0, 0
        for i in range(1, rows * 2 + 1):
            answer[c][r] = i

            if i % 2 == 1:
                if r == rows - 1:
                    r = 0
                else:
                    r += 1
            else:
                c += 1


    else:
        r, c = 0, 0
        num = 1
        while True:
            if zeros == 0:
                break

            if answer[c][r] == 0:
                zeros -= 1

            answer[c][r] = num

            if num % 2 == 1:
                # 홀수
                if r == columns - 1:
                    r = 0
                else:
                    r += 1

            else:
                # 짝수
                if c == rows - 1:
                    c = 0
                else:
                    c += 1

            num += 1

    return answer