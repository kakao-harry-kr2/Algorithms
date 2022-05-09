import time

MAX = 200000
BIG_NUMBER = 10 ** 9 + 7

# tree에 k를 추가
def add(tree, node, start, end, k):
    tree[node][0] += 1
    tree[node][1] += k # tree[node][1] = (tree[node][1] + k) % BIG_NUMBER

    # leaf node
    if start == end:
        return

    if k <= (start + end) // 2:
        add(tree, 2*node, start, (start+end)//2, k)
    else: 
        add(tree, 2*node+1, (start+end)//2+1, end, k)

# [start, end] 범위에 존재하는 숫자들의 개수 & 합
def search(tree, node, start, end, left, right):
    if left > end or right < start:
        return 0, 0
    
    if left <= start and end <= right:
        return tree[node]

    cnt1, sum1 = search(tree, 2*node, start, (start+end)//2, left, right)
    cnt2, sum2 = search(tree, 2*node+1, (start+end)//2+1, end, left, right)

    return cnt1 + cnt2, (sum1 + sum2) % BIG_NUMBER

start = time.time()

# N = int(input())
N = 200000
tree = [[0, 0] for _ in range(2 ** 20)]

answer = 1
for i in range(N):
    # x = int(input())
    x = 199990

    if i != 0:
        lc, ls = search(tree, 1, 0, MAX, 0, x)
        rc, rs = i - lc, tree[1][1] - ls

        val_l = lc * x - ls
        val_r = rs - rc * x
        
        answer = answer * (val_l + val_r + BIG_NUMBER) % BIG_NUMBER

    add(tree, 1, 0, MAX, x)

end = time.time()

print(end - start)
print(answer)