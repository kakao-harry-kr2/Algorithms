from collections import deque

def bfs(t, graph, visited):
    q = deque([[0, 0]])
    visited[0] = True
    
    while q:
        depth, now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                if i == t:
                    return depth+1
                
                visited[i] = True
                q.append([depth+1, i])
    
    return 0
            
def solution(begin, target, words):
    L = len(begin)
    N = len(words)
    graph = [[] for _ in range(N+1)]
    
    words = [begin] + words
    for i in range(N):
        for j in range(i+1, N+1):
            diff = 0
            for k in range(L):
                if words[i][k] != words[j][k]:
                    diff += 1
            if diff == 1:
                graph[i].append(j)
                graph[j].append(i)
    
    try:
        t = words.index(target)
    except:
        return 0
    
    visited = [False] * (N+1)
    
    return bfs(t, graph, visited)

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))