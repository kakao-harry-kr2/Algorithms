import sys
sys.setrecursionlimit(10 ** 4)

def dfs(dp, num, links, now, L):
    if dp[now][0] != None:
        return
    
    left, right = links[now]

    # leaf node인 경우
    if left == -1 and right == -1:
        dp[now] = [1, num[now]]
        return
    
    if left != -1:
        dfs(dp, num, links, left, L)
    if right != -1:
        dfs(dp, num, links, right, L)
    
    # left child만 있는 경우
    if right == -1:
        if num[now] + dp[left][1] <= L:
            dp[now] = [dp[left][0], dp[left][1] + num[now]]
        else:
            dp[now] = [dp[left][0] + 1, num[now]]
        return
    
    # right child만 있는 경우
    if left == -1:
        if num[now] + dp[right][1] <= L:
            dp[now] = [dp[right][0], dp[right][1] + num[now]]
        else:
            dp[now] = [dp[right][0] + 1, num[now]]
        return
    
    # 자식 노드가 2개인 경우
    if num[now] + dp[left][1] + dp[right][1] <= L:
        dp[now] = [dp[left][0]+dp[right][0]-1, num[now] + dp[left][1] + dp[right][1]]
    elif num[now] + dp[left][1] <= L or num[now] + dp[right][1] <= L:
        dp[now] = [dp[left][0]+dp[right][0], num[now] + min(dp[left][1], dp[right][1])]
    else:
        dp[now] = [dp[left][0]+dp[right][0]+1, num[now]]

def solution(k, num, links):
    answer = 0
    N, summation = len(num), sum(num)
    start, end = max(max(num), summation // k), summation
    while start <= end:
        L = (start + end) // 2
        dp = [[None, None] for _ in range(N)]
        for i in range(N):
            dfs(dp, num, links, i, L)
        
        max_count = 0
        for i in range(N):
            max_count = max(max_count, dp[i][0])
        
        if max_count <= k:
            answer = L
            end = L - 1
        else:
            start = L + 1

    return answer