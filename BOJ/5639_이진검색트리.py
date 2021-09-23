import sys

sys.setrecursionlimit(20_000)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert_value(self.root, value)
        return

    def _insert_value(self, node, value):
        if node is None:
            return Node(value)
        else:
            if node.value <= value:
                node.right = self._insert_value(node.right, value)
            else:
                node.left = self._insert_value(node.left, value)
        return node

    def postOrder(self):
        if self.root is not None:
            self._postOrder(self.root)
        return

    def _postOrder(self, node):
        if node.left is not None:
            self._postOrder(node.left)

        if node.right is not None:
            self._postOrder(node.right)

        print(node.value)
        return


bst = BinarySearchTree()
while True:
    try:
        bst.insert(int(sys.stdin.readline().strip()))
    except:
        break
bst.postOrder()


"""
전위 순회한 순서대로 이진트리를 만들고
만들어진 이진트리를 후위순회 하는 방식
"""