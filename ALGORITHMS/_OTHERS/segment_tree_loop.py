def init(tree, N):
    for i in reversed(range(1, N)):
        tree[i] = tree[i << 1] + tree[i << 1 | 1]

numList = [1, 3, 5, 2, 6, 4]
print(f'numList: {numList}')
N = len(numList)
tree = [0] * (2 * N)

for i in range(N):
    tree[N + i] = numList[i]

init(tree, N)
print(f'tree : {tree}')

def query(tree, N, left, right):
    result = 0
    left += N
    right += N
    while left < right:
        if left % 2 == 1:
            result += tree[left]
            left += 1
        if right % 2 == 1:
            result += tree[right - 1]
            right -= 1
        left //= 2
        right //= 2
    return result

print(f'idx 1 to 3 : {numList[1:4]}')
print(f'sum 1 to 3 : {query(tree, N, 1, 4)}')

def update(tree, N, i, val):
    tree[N + i] = val
    i += N
    while i > 1:
        tree[i >> 1] = tree[i] + tree[i ^ 1]
        i >>= 1

update(tree, N, 1, 4)
numList[1] = 4
print(f'idx 1 to 3 : {numList[1:4]}')
print(f'sum 1 to 3 : {query(tree, N, 1, 4)}')