class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


def travel_preorder(node):
    print(node.value, end="")
    if node.left != ".":
        travel_preorder(tree[node.left])
    if node.right != ".":
        travel_preorder(tree[node.right])


def travel_inorder(node):
    if node.left != ".":
        travel_inorder(tree[node.left])
    print(node.value, end="")
    if node.right != ".":
        travel_inorder(tree[node.right])


def traver_postorder(node):
    if node.left != ".":
        traver_postorder(tree[node.left])
    if node.right != ".":
        traver_postorder(tree[node.right])
    print(node.value, end="")


import sys

_n = int(input())
tree = {}

for i in range(_n):
    node, left, right = map(str, input().split())
    # node, left, right = [sys.stdin.readline().split() for _ in range(_n)]
    tree[node] = Node(value=node, left=left, right=right)

travel_preorder(tree["A"])
print()
travel_inorder(tree["A"])
print()
traver_postorder(tree["A"])
print()