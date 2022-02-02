N, M = map(int, input().split())

memoryList = list(map(int, input().split()))
costList = list(map(int, input().split()))

visit = [0] * 10001
table = [0] * 10001
visit[0] = 1
table[0] = 0

for i in range(N):
    for j in reversed(range(10001)):
        if visit[j] == 1:
            k = j + costList[i]
            table[k] = max(table[j] + memoryList[i], table[k])
            visit[k] = 1

for j in range(10001):
    if table[j] >= M:
        print(j)
        break