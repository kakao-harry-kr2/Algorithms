# 트리의 순회

import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

pos = [0] * (n + 1)
for i in range(n):
    pos[inorder[i]] = i


def preorder(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return

    root_value = postorder[post_end]
    print(root_value, end=' ')

    root_index = pos[root_value]
    
    left_child_len = root_index - in_start
    right_child_len = in_end - root_index

    preorder(in_start, in_start + left_child_len - 1, post_start, post_start + left_child_len - 1)
    preorder(in_end - right_child_len + 1, in_end, post_end - right_child_len, post_end - 1)

preorder(0, n-1, 0, n-1)