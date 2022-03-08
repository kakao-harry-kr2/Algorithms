# 요세푸스 문제 2

def init(tree, node, start, end):
    global N
    if start == end:
        tree[node] = 1
        return
    
    tree[node] = end - start + 1

    init(tree, node*2, start, (start+end)//2)
    init(tree, node*2+1, (start+end)//2+1, end)

def find(tree, k):
    global N
    node, start, end = 1, 0, N - 1

    while start < end:
        tree[node] -= 1
        mid = (start + end) // 2
        if k <= tree[node*2]:
            end = mid
            node = node * 2
        else:
            start = mid + 1
            k -= tree[node*2]
            node = node * 2 + 1
    
    tree[node] -= 1
    return start + 1

N, K = map(int, input().split())
tree = [0] * (2 ** 18)

init(tree, 1, 0, N-1)

count = 0
ansList = []
k = 1

while count < N:
    k = (k + K - 2) % (N - count) + 1
    ansList.append(find(tree, k))
    count += 1

print("<%d" % K, end='')
for ans in ansList[1:]:
    print(", %d" % ans, end='')
print(">")