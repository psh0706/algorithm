from itertools import combinations
import copy

N, k = map(int, input().split())
length = len(str(N))
comb = list(combinations(range(0, length), 2))
maxi = 0

# def recursion(depth, result):
#     global maxi
#     if depth == k:
#         r = int(''.join(map(str, result)))
#         maxi = max(maxi, r)
#         return
#
#     for c in comb:
#         a = c[0]
#         b = c[1]
#
#         temp = copy.deepcopy(result)
#         temp[a] = result[b]
#         temp[b] = result[a]
#         mt = list(map(int, str(maxi)))
#         if temp[0] == 0:
#             continue
#
#         recursion(depth + 1, temp)
#
#
# if length == 1:
#     print(-1)
# else:
#     recursion(0, NList)
#     if maxi == 0:
#         print(-1)
#     else:
#         print(maxi)

if N < 10:
    print(-1)
else:
    q = [N]
    cnt = 0

    while q:
        size = len(q)
        level = []
        flag = True
        for i in range(size):
            li = list(map(int, str(q.pop(0))))
            for c in comb:
                a = c[0]
                b = c[1]
                temp = copy.deepcopy(li)
                temp[a] = li[b]
                temp[b] = li[a]

                if temp[0] != 0:
                    r = int(''.join(map(str, temp)))
                    if r not in level:
                        level.append(r)
                        q.append(r)

        cnt += 1

        if cnt == k:
            if level:
                maxi = max(level)
            else:
                maxi = -1
            break

    if cnt < k:
        print(-1)
    else:
        print(maxi)


"""
재귀로 접근했다가 시간초과 폭탄..
재귀 > 시간초과 > 가지치기를 해보자! > 시간초과 테크를 탄 후에야 
bfs 로 접근해야함을 알 수 있었다..!
가지치기는 매 depth 마다 중복되는 노드를 제거하는 방향으로 했다.
생각보다 빨리 풀어서 기분좋았던 문제 :)
"""