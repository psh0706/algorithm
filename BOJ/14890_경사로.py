def check(temp, L, N):
    now = -1
    hill = [False for _ in range(N)]
    flag = False

    for i in range(N):
        if i == N - 1:
            flag = True
            break

        now = temp[i]

        if now == temp[i + 1]:
            continue

        elif now - temp[i + 1] == 1:
            flat = 0
            for l in range(1, L + 1):
                if i + l < N and not hill[i + l] and temp[i + l] == temp[i + 1]:
                    flat += 1
                else:
                    break

            if flat == L:
                for l in range(1, L + 1):
                    hill[i + l] = True
                continue
            else:
                break

        elif now - temp[i + 1] == -1:
            flat = 0
            for l in range(L):
                if i - l >= 0 and not hill[i - l] and temp[i - l] == now:
                    flat += 1
                else:
                    break

            if flat == L:
                for l in range(L):
                    hill[i - l] = True
                continue
            else:
                break
        else:
            break

    if flag:
        return True

    return False


def solution():
    N, L = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    for i in range(N):
        tempV = MAP[i]
        if check(tempV, L, N):
            answer += 1

        tempH = [line[i] for line in MAP]
        if check(tempH, L, N):
            answer += 1

    print(answer)


solution()


"""
구현 문제
현재 칸의 고도보다 차이가 나는 칸을 마주쳤을 시 경사로를 놓을 수 있는지 체크한다.
이미 경사로가 놓인 칸에는 경사로를 다시 놓을 수 없음에 주의한다 (겹치거나 올려둘 수 없다.) -> hill 리스트를 이용해서 방문처리 함으로 해결.
"""