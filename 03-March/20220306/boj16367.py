# TV Show Game

from itertools import permutations
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def num2node(k, num):
    if num < 0:
        return k - num
    else:
        return num

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

def flip(k, num):
    if num > k:
        return num - k
    else:
        return num + k

k, n = map(int, input().split())
graph = [[] for _ in range(2 * k + 1)]
reverse_graph = [[] for _ in range(2 * k + 1)]

for _ in range(n):
    l1, c1, l2, c2, l3, c3 = input().split()

    l1 = int(l1) if c1 == 'R' else -int(l1)
    l2 = int(l2) if c2 == 'R' else -int(l2)
    l3 = int(l3) if c3 == 'R' else -int(l3)

    for perm in permutations([l1, l2, l3], 2):
        graph[num2node(k, -perm[0])].append(num2node(k, perm[1]))
        reverse_graph[num2node(k, perm[0])].append(num2node(k, -perm[1]))

stack = []
visited = [False] * (2 * k + 1)

for i in range(1, 2 * k + 1):
    if not visited[i]:
        dfs(i, visited, stack)

visited = [False] * (2 * k + 1)
result = []

while stack:
    scc = []
    node = stack.pop()
    if not visited[node]:
        reverse_dfs(node, visited, scc)
        result.append(scc)

num2scc = [None] * (2 * k + 1)

for i in range(len(result)):
    for r in result[i]:
        num2scc[r] = i

for i in range(1, k + 1):
    if num2scc[i] == num2scc[k + i]:
        print(-1)
        exit()

value = [None] * (2 * k + 1)

for i in range(len(result)):
    for r in result[i]:
        if value[r] == None:
            value[r] = 'B'
            value[flip(k, r)] = 'R'

for i in range(1, k + 1):
    print(value[i], end='')