def solution(grid, clockwise):
    answer = []
    length = len(grid)
    if clockwise:
        for i in range(length, 0, -1):
            result = ''

            idx = length - 1
            for j in range(len(grid) - i, 0, -1):
                k = j * 2 - 1
                result += grid[idx][k:k + 2][::-1]
                idx -= 1

            result += grid[i - 1][0]

            answer.append(result)

    else:
        for i in range(length):
            grid[i] = grid[i][::-1]

        for i in range(length, 0, -1):
            result = grid[i - 1][0]
            idx = length - 1
            temp = ''
            for j in range(len(grid) - i, 0, -1):
                k = j * 2 - 1
                temp = grid[idx][k:k + 2] + temp
                idx -= 1
            result += temp
            answer.append(result)

    return answer