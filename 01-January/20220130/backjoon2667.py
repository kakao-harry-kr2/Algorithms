import sys
input = sys.stdin.readline

N = int(input())
table = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

countList = []
count = 0

x_list = [0, 0, -1, 1]
y_list = [-1, 1, 0, 0]

def bfs(i, j):
    global count
    for k in range(4):
        next_i, next_j = i + x_list[k], j + y_list[k]
        if 0 <= next_i < N and 0 <= next_j < N and table[next_i][next_j] == 1 and not visited[next_i][next_j]:
            visited[next_i][next_j] = True
            count += 1
            bfs(next_i, next_j)

for i in range(N):
    for j in range(N):
        if table[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            count = 1
            bfs(i, j)
            countList.append(count)

print(len(countList))
countList.sort()
for count in countList:
    print(count)