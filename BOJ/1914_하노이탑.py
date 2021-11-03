N = int(input())
result = ""
# cnt = 0


def hanoi(depth, st, ed, m):
    # global cnt
    if depth == 1:
        print(str(st) + " " + str(ed))
        # cnt += 1
        return

    hanoi(depth-1, st, m, ed)
    print(str(st) + " " + str(ed))
    # cnt += 1
    hanoi(depth-1, m, ed, st)


print(2**N-1)
if N <= 20:
    hanoi(N, 1, 3, 2)
    # print(cnt)
    print(result)


"""
웰-노운 재귀 문제 하노이탑
하노이탑은 N개의 원판에 대해서 2^N-1의 최소 이동 횟수를 가진다.

st: 시작 고리
ed: 목적 고리
m : 두 고리를 제외한 고리

가장 밑에 있는 판을 목적지인 3번째 고리에 옮긴다는것을 전제로 재귀를 시작한다.
가장 밑 판이 움직이기 위해서는 그 위의 탑이 2번 고리로 옮겨져야 한다. (st -> m)
탑이 2번으로 옮겨졌다면 가장 밑판을 3번으로 이동시킨다 (st -> ed)
2번고리의 탑을 3번 고리로 모두 이동시킨다. 합체 (m -> ed)

위의 과정을 재귀적으로 진행한다.
"""