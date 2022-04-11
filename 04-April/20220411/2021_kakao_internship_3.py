import time

def init(tree, node, start, end):
    tree[node] = end - start + 1
    if start + 2 > end:
        return
    mid = (start+end)//2
    init(tree, node*2, start, mid)
    init(tree, node*2+1, mid+1, end)

# index번째로 작은 수
def find(tree, n, index):
    node, start, end = 1, 0, n-1
    while start < end:
        mid = (start+end)//2
        v = tree[node*2]
        if index <= v:
            end = mid
            node = node * 2
        else:
            index -= v
            start = mid + 1
            node = node * 2 + 1

    return start

# number를 subnode로 가지는 모든 node에 +value
def update(tree, n, number, value):
    node, start, end = 1, 0, n-1
    while start < end:
        mid = (start+end)//2
        tree[node] += value

        if number <= mid:
            end = mid
            node = node * 2
        else:
            start = mid + 1
            node = node * 2 + 1
    
    tree[node] += value

def solution(n, k, cmd):
    numList = ['O'] * n
    stack = []

    tree = [1] * (2 ** 21)
    init(tree, 1, 0, n-1)

    index = k + 1
    number = k

    for command in cmd:
        if command[0] == 'U':
            index -= int(command[2:])
            number = find(tree, n, index)
        
        elif command[0] == 'D':
            index += int(command[2:])
            number = find(tree, n, index)
        
        elif command[0] == 'C':
            if index == tree[1]:
                index -= 1

            stack.append(number)
            numList[number] = 'X'
            update(tree, n, number, -1)
            number = find(tree, n, index)

        else:
            num = stack.pop()
            numList[num] = 'O'
            if num < number:
                index += 1
            update(tree, n, num, 1)

    return ''.join(numList)

n = 1000000
k = 999999
cmd = ['C'] * 200000

start = time.time()

solution(n, k, cmd)

end = time.time()

print(end - start)