import sys

R, C = map(int, sys.stdin.readline().split())
yard = [list(sys.stdin.readline().strip()) for _ in range(R)]
visit = [[True for _ in range(C)] for _ in range(R)]


def sheep():
    q = []
    O, V = 0, 0

    for i in range(R):
        for j in range(C):
            localO = 0
            localV = 0
            if visit[i][j]:
                q.append({'x': i, 'y': j})
                visit[i][j] = False
            else:
                continue

            while len(q) != 0:
                n = q.pop(0)

                if yard[n['x']][n['y']] == 'v':
                    localV += 1
                elif yard[n['x']][n['y']] == 'o':
                    localO += 1
                elif yard[n['x']][n['y']] == '#':
                    continue

                if n['x'] - 1 >= 0 and visit[n['x'] - 1][n['y']] and yard[n['x'] - 1][n['y']] != "#":
                    visit[n['x'] - 1][n['y']] = False
                    q.append({'x': n['x'] - 1, 'y': n['y']})
                if n['x'] + 1 < R and visit[n['x'] + 1][n['y']] and yard[n['x'] + 1][n['y']] != "#":
                    visit[n['x'] + 1][n['y']] = False
                    q.append({'x': n['x'] + 1, 'y': n['y']})
                if n['y'] - 1 >= 0 and visit[n['x']][n['y'] - 1] and yard[n['x']][n['y'] - 1] != "#":
                    visit[n['x']][n['y'] - 1] = False
                    q.append({'x': n['x'], 'y': n['y'] - 1})
                if n['y'] + 1 < C and visit[n['x']][n['y'] + 1] and yard[n['x']][n['y'] + 1] != "#":
                    visit[n['x']][n['y'] + 1] = False
                    q.append({'x': n['x'], 'y': n['y'] + 1})

            if localO <= localV:
                V += localV
            else:
                O += localO

    return O, V


resultO, resultV = sheep()
print(str(resultO)+" "+str(resultV))
