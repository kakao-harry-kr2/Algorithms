# 최종 순위

from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    scoreList = list(map(lambda x: int(x) - 1, input().split()))

    graph = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            graph[scoreList[i]][scoreList[j]] = 1

    m = int(input())
    for _ in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())
        graph[a][b] = 1 - graph[a][b]
        graph[b][a] = 1 - graph[b][a]

    indegree = [0] * n

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                indegree[j] += 1

    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque()

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)
    
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now+1)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for j in range(n):
            if graph[now][j] == 1:
                indegree[j] -= 1
                # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                if indegree[j] == 0:
                    q.append(j)

    if len(result) == n:
        print(*result)
    else:
        print("IMPOSSIBLE")