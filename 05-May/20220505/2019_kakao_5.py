import sys
sys.setrecursionlimit(10000)

def preorder(graph, node, preList:list):
    preList.append(node)
    if graph[node][0] != -1:
        preorder(graph, graph[node][0], preList)
    if graph[node][1] != -1:
        preorder(graph, graph[node][1], preList)

def postorder(graph, node, postList:list):
    if graph[node][0] != -1:
        postorder(graph, graph[node][0], postList)
    if graph[node][1] != -1:
        postorder(graph, graph[node][1], postList)
    postList.append(node)

def solution(nodeinfo:list):
    N = len(nodeinfo)
    depth = [[] for _ in range(100001)]
    for i in range(N):
        depth[nodeinfo[i][1]].append((i+1, nodeinfo[i][0]))

    graph = [[-1, -1] for _ in range(N+1)]
    rangeList = [None] * (N+1)

    y = 100000
    while not depth[y]:
        y -= 1
    
    root = depth[y][0][0]
    rangeList[depth[y][0][0]] = (0, 100000)
    while True:
        next_y = y - 1
        while next_y >= 0 and not depth[next_y]:
            next_y -= 1
        
        if next_y == -1:
            break
        
        depth[next_y].sort(key=lambda x: x[1])

        i, j = 0, 0
        while j < len(depth[next_y]):
            if rangeList[depth[y][i][0]][0] <= depth[next_y][j][1] <= rangeList[depth[y][i][0]][1]:
                if depth[next_y][j][1] < depth[y][i][1]:
                    graph[depth[y][i][0]][0] = depth[next_y][j][0]
                    rangeList[depth[next_y][j][0]] = (rangeList[depth[y][i][0]][0], depth[y][i][1]-1)
                else:
                    graph[depth[y][i][0]][1] = depth[next_y][j][0]
                    rangeList[depth[next_y][j][0]] = (depth[y][i][1]+1, rangeList[depth[y][i][0]][1])

                j += 1
            else:
                i += 1
        
        y = next_y

    preList, postList = [], []
    preorder(graph, root, preList)
    postorder(graph, root, postList)

    answer = [preList, postList]
    return answer

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
# nodeinfo = [[5,3]]
print(solution(nodeinfo))