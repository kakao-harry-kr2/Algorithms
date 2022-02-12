# 트리

import sys
input = sys.stdin.readline

def getParent(parent, x):
    if parent[x] != x:
        parent[x] = getParent(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x = getParent(parent, x)
    y = getParent(parent, y)

    if x == y:
        return 0

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

    return 1

case_number = 0

while True:
    case_number += 1
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    parent = [i for i in range(n + 1)]

    cycle_element = [0] * (n + 1)

    for _ in range(m):
        x, y = map(int, input().split())
        
        if x == y:
            continue
        
        x_parent = parent[x]
        y_parent = parent[y]

        ret = union(parent, x, y)
        if ret == 0:
            cycle_element[x] = 1
    
    root_node = [0] * (n + 1)
    cycle = [0] * (n + 1)

    for i in range(1, n + 1):
        root_node[getParent(parent, i)] = 1
        if cycle_element[i] == 1:
            cycle[parent[i]] = 1
    
    T = sum(root_node) - sum(cycle)

    print("Case {}:".format(case_number), end=' ')

    if T == 0:
        print("No trees.")
    
    elif T == 1:
        print("There is one tree.")
    
    else:
        print("A forest of {} trees.".format(T))