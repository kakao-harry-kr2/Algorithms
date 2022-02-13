# 트리의 독립집합

import sys
input = sys.stdin.readline

def dfs(graph, visited, children, start):
    visited[start] = True
    for node in graph[start]:
        if not visited[node]:
            children[start].append(node)
            dfs(graph, visited, children, node)

def max_independent_set(children, dp, w_list, start):
    # 이미 해당 노드에 대한 계산을 한 경우
    if dp[start] != [-1, -1]:
        return dp[start]
    
    # 해당 노드를 포함한 최대 독립 집합
    answer1 = 0
    # 해당 노드를 포함하지 않는 최대 독립 집합
    answer2 = 0

    for child in children[start]:
        include, exclude = max_independent_set(children, dp, w_list, child)
        answer1 += exclude
        answer2 += max(include, exclude)
    
    # 해당 노드 포함 처리
    answer1 += w_list[start]

    dp[start] = [answer1, answer2]

    return [answer1, answer2]

def backtrace(children, answerList, dp, start, type):
    if type == 1:
        answerList.append(start)
        
        for child in children[start]:
            backtrace(children, answerList, dp, child, 0)
    
    else:
        for child in children[start]:
            if dp[child][0] > dp[child][1]:
                backtrace(children, answerList, dp, child, 1)
            else:
                backtrace(children, answerList, dp, child, 0)

n = int(input())
w_list = [0] + list(map(int, input().split()))

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(n-1):
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)

# 각 노드들의 자식 노드
children = [[] for _ in range(n+1)]

dfs(graph, visited, children, 1)

# dp[node] -> 
# 첫번째 요소 : 해당 노드를 포함하는 서브트리에서의 최대 독립 집합
# 두번째 요소 : 해당 노드를 포함하지 않는 서브트리에서의 최대 독립 집합
dp = [[-1, -1] for _ in range(n+1)]

answer = max_independent_set(children, dp, w_list, 1)

print(max(answer))

t = 1 if answer[0] > answer[1] else 0
answerList = []

backtrace(children, answerList, dp, 1, t)

answerList.sort()

print(*answerList)