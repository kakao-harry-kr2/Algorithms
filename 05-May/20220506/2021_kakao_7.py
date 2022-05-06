def dfs(graph, dp, now):
    if not graph[now]:
        return
    
    children = []
    for child in graph[now]:
        dfs(graph, dp, child)
        children.append(dp[child])
    
    ok = False
    for child in children:
        dp[now][0] += min(child)
        dp[now][1] += min(child)
        if child[0] <= child[1]:
            ok = True
    
    if ok: return

    diff = [child[0] - child[1] for child in children]
    dp[now][1] += min(diff)
    return


def solution(sales, links):
    N = len(sales)

    graph = [[] for _ in range(N+1)]
    for a, b in links:
        graph[a].append(b)

    dp = [[sales[i-1], 0] for i in range(N+1)]

    dfs(graph, dp, 1)

    return min(dp[1])

sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
print(solution(sales, links))