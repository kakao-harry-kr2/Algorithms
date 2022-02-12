# 이진 검색 트리

import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break

def postorder(start, end):
    if start > end:
        return
    
    root_node = preorder[start]

    index = start + 1
    while index <= end and preorder[index] < root_node:
        index += 1
    
    left_count = index - start - 1
    right_count = end - start - left_count

    postorder(start + 1, start + left_count)
    postorder(end - right_count + 1, end)

    print(root_node)

postorder(0, len(preorder)-1)
