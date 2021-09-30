import sys
from string import ascii_uppercase
sys.setrecursionlimit(20_000)

N = int(sys.stdin.readline())
key = list(ascii_uppercase)
tree = dict.fromkeys(key)
for t in tree:
    tree[t] = {'left': None, 'right': None}

for i in range(N):
    root, left, right = sys.stdin.readline().split()
    if not left == '.':
        tree[root]['left'] = left
    if not right == '.':
        tree[root]['right'] = right


def preOrder(node):
    global pre_order
    pre_order += node

    if tree[node]['left'] is not None:
        preOrder(tree[node]['left'])

    if tree[node]['right'] is not None:
        preOrder(tree[node]['right'])

    return


def inOrder(node):
    global in_order

    if tree[node]['left'] is not None:
        inOrder(tree[node]['left'])

    in_order += node

    if tree[node]['right'] is not None:
        inOrder(tree[node]['right'])

    return


def postOrder(node):
    global post_order

    if tree[node]['left'] is not None:
        postOrder(tree[node]['left'])

    if tree[node]['right'] is not None:
        postOrder(tree[node]['right'])

    post_order += node

    return


pre_order = in_order = post_order = ''

preOrder('A')
inOrder('A')
postOrder('A')

print(pre_order)
print(in_order)
print(post_order)

"""
간단한 트리 순회 문제
해시맵(딕셔너리) 로 트리를 구현해서 풀었다.
조건 중 N의 최대가 26이라는것을 보고 알파벳으로 key 만들어서 해시맵 설계했다
"""