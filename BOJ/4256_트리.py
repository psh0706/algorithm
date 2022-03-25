class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


def makeTree(inorder, preorder):
    value = preorder[0]
    rootIdx = inorder.index(value)

    leftIn = inorder[0:rootIdx]
    rightIn = inorder[rootIdx+1:]

    leftPre = preorder[1:len(leftIn)+1]
    rightPre = preorder[1+len(leftIn):]

    if len(leftIn) > 0 and len(leftPre) > 0:
        left = makeTree(leftIn, leftPre)
    else:
        left = None

    if len(rightIn) > 0 and len(rightPre) > 0:
        right = makeTree(rightIn, rightPre)
    else:
        right = None

    return Node(value, left, right)


def postOrder(root):
    if root is None:
        return ""
    return postOrder(root.left) + postOrder(root.right) + str(root.value)+" "


def solution():
    T = int(input())
    for _ in range(T):
        n = int(input())
        preOrder = list(map(int, input().split()))
        inOrder = list(map(int, input().split()))

        root = makeTree(inOrder, preOrder)
        print(postOrder(root))


solution()

"""
preorder 는 항상 맨앞이 root 이고, 그 뒤로 좌 -> 우 순서로 자식 트리가있다는 특성과
inorder 는 항상 좌-> root -> 우 순서로 자식 트리가 있다는 특성을 이용.

preorder 를 통해 root 값의 value 를 알아낸다.
그리고 inorder 를 통해 왼쪽 자식트리와 오른쪽 자식 트리의 개수를 파악하고
그것을 기준으로 다시 왼쪽, 오른쪽 inorder, preorder 트리를 만들어 재귀적으로 넘겨준다.

트리가 완성된 후에는 후위순회하는 재귀함수를 한번 더 돌려주었다.
"""