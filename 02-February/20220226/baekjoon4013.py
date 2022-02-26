# ATM

import heapq
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
reverse_graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    reverse_graph[B].append(A)

# 각 교차로에서 인출할 수 있는 현금 금액
moneyList = [None]
for i in range(N):
    moneyList.append(int(input()))

# 출발지점 S, 레스토랑의 수 P
S, P = map(int, input().split())
restaurants = list(map(int, input().split()))

def dfs(start:int, visited:list, stack:list):
    visited[start] = True
    for node in graph[start]:
        if not visited[node]:
            dfs(node, visited, stack)
    
    stack.append(start)

def reverse_dfs(start:int, visited:list, stack:list):
    visited[start] = True
    stack.append(start)
    for node in reverse_graph[start]:
        if not visited[node]:
            reverse_dfs(node, visited, stack)

stack = []
visited = [False] * (N + 1)

for i in range(1, N + 1):
    if not visited[i]:
        dfs(i, visited, stack)

visited = [False] * (N + 1)
result = []

while stack:
    scc = []
    node = stack.pop()
    if not visited[node]:
        reverse_dfs(node, visited, scc)
        result.append(scc)

# SCC 관계를 그래프로
node2scc = [None] * (N + 1)
n = len(result)
weightList = [0] * n

for i in range(n):
    for res in result[i]:
        node2scc[res] = i
        weightList[i] += moneyList[res]

# 그래프에서 최고 금액 탐색 (다익스트라)

start = node2scc[S]
scc_graph = [[] for _ in range(n)]
distance = [0] * n

# 레스토랑이 있는 SCC 탐색
scc_restaurents = [False] * n

for restaurent in restaurants:
    scc_restaurents[node2scc[restaurent]] = True

for i in range(1, N + 1):
    for j in graph[i]:
        if node2scc[i] != node2scc[j]:
            scc_graph[node2scc[i]].append(node2scc[j])

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 weightList[start]으로 설정하여, 큐에 삽입
    heapq.heappush(q, (weightList[start], start))
    distance[start] = weightList[start]
    while q:
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] > dist:
            continue

        for i in scc_graph[now]:
            cost = dist + weightList[i]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost > distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

dijkstra(start)

max_value = 0
for i in range(n):
    if scc_restaurents[i]:
        max_value = max(max_value, distance[i])

print(max_value)