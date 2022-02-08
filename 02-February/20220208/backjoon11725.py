import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [-1] * (N + 1)
parent[1] = 0

def makeTree(now):
    for node in graph[now]:
        if parent[node] == -1:
            parent[node] = now
            makeTree(node)

makeTree(1)

for i in range(2, N + 1):
    print(parent[i])