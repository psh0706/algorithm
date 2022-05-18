n = int(input())
item = "*"
stars = [[" " for _ in range(n)] for _ in range(n)]


def dfs(length, r, c):
    if length == 1:
        stars[r][c] = "*"
        return

    m = length // 3
    rList = [r]
    cList = [c]

    for i in range(3):
        rList.append(rList[-1]+m)
        cList.append(cList[-1]+m)

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            dfs(m, rList[i], cList[j])


dfs(n, 0, 0)

for star in stars:
    print(''.join(star))


"""
재귀를 사용해서 풀어본 별 찍기
n*n 사이즈의 배열을 만들어놓고 시작.

3*3, 총 9개의 블럭 공간이 있다는 개념으로 접근해서
각 블럭을 계속 3개로 쪼개들어간다. (각 경우의 x와 y 값을 계속 구해준다.)
더이상 쪼갤 수 없으면 * 를 그 위치에 저장하는 방식.
모양에 맞게 가운데 부분은 재귀로 들어가지 않는다.
"""