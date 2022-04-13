INF = 10 ** 9

# root를 포함한 값도 같이 넘겨주어야 할듯?
def search(graph, visited, num, dp, k, now):
    visited[now] = True
    children = []

    for node in graph[now]:
        if not visited[node]:
            children.append(node)
            search(graph, visited, num, dp, k, node)

    # leaf node인 경우
    if len(children) == 0:
        dp[now].append([num[now], num[now]])

    # 자식 노드가 하나인 경우
    elif len(children) == 1:
        child = children[0]
        dp[now] = [[INF, INF] for _ in range(min(k, len(dp[child]) + 1))]
        for i in range(len(dp[child])):
            # now와 node사이의 edge를 끊지 않는 경우
            new_top = num[now] + dp[child][i][0]
            new_max = max(dp[child][i][0] + num[now], dp[child][i][1])
            if new_max < dp[now][i][1]:
                dp[now][i] = [new_top, new_max]
            # now와 node사이의 edge를 끊는 경우
            if i + 1 < k:
                new_top = num[now]
                new_max = max(num[now], dp[child][i][1])
                if new_max < dp[now][i+1][1]:
                    dp[now][i+1] = [new_top, new_max]

    # 자식 노드가 2개인 경우
    else:
        left_child, right_child = children
        dp[now] = [[INF, INF] for _ in range(min(k, len(dp[left_child]) + len(dp[right_child]) + 1))]
        for i in range(len(dp[left_child])):
            for j in range(len(dp[right_child])):
                # 추가적으로 끊지 않는 경우
                if i + j < k:
                    new_top = num[now] + dp[left_child][i][0] + dp[right_child][j][0]
                    new_max = max(new_top, dp[left_child][i][1], dp[right_child][j][1])
                    if new_max < dp[now][i+j][1]:
                        dp[now][i+j] = [new_top, new_max]
                
                # left_child만 끊는 경우
                if i + j + 1 < k:
                    new_top = num[now] + dp[right_child][j][0]
                    new_max = max(new_top, dp[left_child][i][1], dp[right_child][j][1])
                    if new_max < dp[now][i+j+1][1]:
                        dp[now][i+j+1] = [new_top, new_max]
                
                # right_child만 끊는 경우
                if i + j + 1 < k:
                    new_top = num[now] + dp[left_child][i][0]
                    new_max = max(new_top, dp[left_child][i][1], dp[right_child][j][1])
                    if new_max < dp[now][i+j+1][1]:
                        dp[now][i+j+1] = [new_top, new_max]
                
                # 둘 다 끊는 경우
                if i + j + 2 < k:
                    new_top = num[now]
                    new_max = max(new_top, dp[left_child][i][1], dp[right_child][j][1])
                    if new_max < dp[now][i+j+2][1]:
                        dp[now][i+j+2] = [new_top, new_max]

    print(now, dp[now])

def solution(k, num, links):
    N = len(num)
    graph = [[] for _ in range(N)]
    for i in range(N):
        for child in links[i]:
            if child != -1:
                graph[i].append(child)
                graph[child].append(i)
    
    visited = [False] * N

    # dp[i][j]: i번째 노드가 root인 tree에서 j개의 그룹으로 나누었을 때 최솟값
    dp = [[] for _ in range(N)]

    search(graph, visited, num, dp, k, 0)

    answer = INF
    for _, value in dp[0]:
        answer = min(answer, value)

    return answer

# k = 3
# num = [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1]
# links = [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]

# print(solution(k, num, links))

num = [6, 9, 7, 5]
links = [[-1, -1], [-1, -1], [-1, 0], [2, 1]]

# for k in [1, 2, 4]:
#     print(solution(k, num, links))

print(solution(2, num, links))