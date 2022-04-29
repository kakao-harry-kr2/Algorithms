# 00:30:28

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cctv = [None, 
[[0], [1], [2], [3]], 
[[0, 2], [1, 3]], 
[[0, 1], [1, 2], [2, 3], [3, 0]], 
[[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], 
[[0, 1, 2, 3]]
]

cctvPos = []
cctvList = []
for i in range(N):
    for j in range(M):
        if 0 < table[i][j] < 6:
            cctvPos.append((i, j))
            cctvList.append(table[i][j])

num_cctv = len(cctvPos)

answer = N * M
def process(idx, directions):
    global answer
    if idx == num_cctv:
        arr = [[True] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if table[i][j] == 0:
                    arr[i][j] = False
        
        for i in range(num_cctv):
            x, y = cctvPos[i]
            dirs = directions[i]
            for dir in dirs:
                next_x, next_y = x + move[dir][0], y + move[dir][1]
                while 0 <= next_x < N and 0 <= next_y < M and table[next_x][next_y] != 6:
                    arr[next_x][next_y] = True
                    next_x, next_y = next_x + move[dir][0], next_y + move[dir][1]
        
        current = 0
        for i in range(N):
            current += arr[i].count(False)
        
        if current < answer:
            answer = current
        
        return

    for dirs in cctv[cctvList[idx]]:
        process(idx+1, directions + [dirs])

process(0, [])


print(answer)