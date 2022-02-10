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
    tree = True

    cycle = [0] * (n + 1)

    for _ in range(m):
        x, y = map(int, input().split())
        
        if x == y:
            continue
        
        x_parent = parent[x]
        y_parent = parent[y]

        ret = union(parent, x, y)
        if ret == 0:
            if x_parent < y_parent:
                cycle[x_parent] = 1
                cycle[y_parent] = 0
            else:
                cycle[y_parent] = 1
                cycle[x_parent] = 0
    
    root_node = [0] * (n + 1)
    
    for par in parent[1:]:
        root_node[par] = 1
    
    print(parent)
    print(cycle)
    T = sum(root_node) - sum(cycle)

    print("Case {}:".format(case_number), end=' ')

    if T == 0:
        print("No trees.")
    
    elif T == 1:
        print("There is one tree.")
    
    else:
        print("A forest of {} trees.".format(T))