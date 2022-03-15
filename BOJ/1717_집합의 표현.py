import sys
sys.setrecursionlimit(10**5)


def find(a):
    if a == head[a]:
        return head[a]
    head[a] = find(head[a])
    return head[a]


def union(a, b):
    aHead = find(a)
    bHead = find(b)

    if aHead == bHead:
        # 이미 같은 집합.
        return

    head[aHead] = bHead
    return


def solution():
    global answer
    for op in ops:
        if op[0] == 0:
            # 합연산
            union(op[1], op[2])
        else:
            # 같은 집합 확인 연산
            if find(op[1]) == find(op[2]):
                answer += 'YES\n'
            else:
                answer += 'NO\n'
    print(answer)


n, m = map(int, input().split())
head = [i for i in range(n + 1)]
ops = [list(map(int, input().split())) for _ in range(m)]
answer = ""
solution()
