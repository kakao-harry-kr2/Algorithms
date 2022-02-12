# 트리 순회

import sys
input = sys.stdin.readline

N = int(input())

children = [[-1, -1] for _ in range(N)]
for _ in range(N):
    parent, left_child, right_child = map(lambda x: ord(x)-65, input().split())
    if 0 <= left_child < 26:
        children[parent][0] = left_child
    if 0 <= right_child < 26:
        children[parent][1] = right_child

def preorder(start):
    left_child = children[start][0]
    right_child = children[start][1]

    print(chr(start+65), end='')

    if left_child != -1:
        preorder(left_child)

    if right_child != -1:
        preorder(right_child)

def inorder(start):
    left_child = children[start][0]
    right_child = children[start][1]

    if left_child != -1:
        inorder(left_child)

    print(chr(start+65), end='')

    if right_child != -1:
        inorder(right_child)

def postorder(start):
    left_child = children[start][0]
    right_child = children[start][1]

    if left_child != -1:
        postorder(left_child)

    if right_child != -1:
        postorder(right_child)

    print(chr(start+65), end='')

preorder(0)
print()
inorder(0)
print()
postorder(0)