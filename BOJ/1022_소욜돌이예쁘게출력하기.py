r1, c1, r2, c2 = map(int, input().split())
piece = [[0 for _ in range(c2 - c1 + 1)] for _ in range(r2 - r1 + 1)]
maxi = max(map(abs, [r1, c1, r2, c2]))
n = maxi * 2 + 1
delta = [[0, -1], [-1, 0], [0, 1], [1, 0]]
value = n * n
x, y = maxi, maxi
digit = 0

while n > 1:
    for i in range(4):
        for j in range(n-1):
            if r1 <= x <= r2 and c1 <= y <= c2:
                digit = max(digit, value)
                piece[x - r1][y - c1] = value

            x += delta[i][0]
            y += delta[i][1]
            value -= 1
    x -= 1
    y -= 1
    n -= 2

if r1 <= 0 <= r2 and c1 <= 0 <= c2:
    piece[r1*-1][c1*-1] = 1

digit = len(str(digit))


for i in range(len(piece)):
    line = ""
    for j in range(len(piece[0])):
        string = str(piece[i][j])
        space = digit - len(string)
        line += " "*space + string + " "
    print(line)


"""
1. 메모리 저장 없이 가상으로 소용돌이 x, y 좌표를 계산함으로써 메모리 제한 극복
    -> 단순 배열로 소용돌이 계산시 10001**2*4/1000000 = 400MB로 메모리 초과
2. r1, c1 ~ r2, c2 범위에 해당하면 배열로 저장.
    -> 출력에 필요한 배열만 저장
3. 저장된 숫자 중 가장 큰 값을 기준으로 자리수를 파악. 자리수 차이 * 공백 수 로 예쁘게 출력 가능 
"""