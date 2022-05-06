from collections import deque

move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
type2block = [
    [(0, 1), (0, 2), (1, 2)], [(0, 1), (1, 0), (2, 0)], [(1, 0), (1, 1), (1, 2)], [(1, 0), (2, 0), (2, -1)],
    [(0, 1), (0, 2), (1, 0)], [(1, 0), (2, 0), (2, 1)], [(1, 0), (1, -1), (1, -2)], [(0, 1), (1, 1), (2, 1)],
    [(1, 0), (1, 1), (1, -1)], [(1, 0), (1, 1), (2, 0)], [(0, 1), (0, 2), (1, 1)], [(1, 0), (2, 0), (1, -1)]
]
erase = [False, False, True, True, False, True, True, False, True, False, False, False]
empty = {2: [1, 2], 3: [-1], 5: [1], 6: [-2, -1], 8: [-1, 1]}
width = [3, 2] * 6

def bfs(board, visited, x, y, val, arr:list):
    N = len(board)
    visited[x][y] = True
    arr.append((x, y))
    for k in range(4):
        next_x, next_y = x + move[k][0], y + move[k][1]
        if 0 <= next_x < N and 0 <= next_y < N and not visited[next_x][next_y] and board[next_x][next_y] == val:
            bfs(board, visited, next_x, next_y, val, arr)

def solution(board):
    answer = 0
    N = len(board)
    visited = [[False] * N for _ in range(N)]
    num2type = [-1] * 201
    num2erase = dict()
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and board[i][j] > 0:
                arr = []
                bfs(board, visited, i, j, board[i][j], arr)
                arr = list(map(lambda x: (x[0]-i, x[1]-j), arr[1:]))
                type_of_block = None
                for k in range(12):
                    if type2block[k] == arr:
                        type_of_block = k
                        break
                
                num2type[board[i][j]] = type_of_block
                if erase[type_of_block]:
                    num2erase[board[i][j]] = [j+col for col in empty[type_of_block]]

    top, height = [None] * N, [None] * N
    for j in range(N):
        i = 0
        while i < N and board[i][j] == 0:
            i += 1
        if i == N:
            continue
        
        top[j] = board[i][j]
        height[j] = i

    while True:
        erasing_step = False
        for j in range(N):
            if top[j] == None:
                continue
            
            num = top[j]
            type_of_block = num2type[num]
            if not erase[type_of_block]:
                continue
            
            h = height[j]
            erasing = True
            for col in num2erase[num]:
                if top[col] != num:
                    erasing = False
                    break
            
            if erasing:
                erasing_step = True
                q = deque([(h, j)])
                while q:
                    now_x, now_y = q.popleft()
                    board[now_x][now_y] = 0
                    for k in range(4):
                        next_x, next_y = now_x + move[k][0], now_y + move[k][1]
                        if 0 <= next_x < N and 0 <= next_y < N and board[next_x][next_y] == num:
                            q.append((next_x, next_y))
                
                answer += 1
                for k in range(N):
                    if height[k] == None:
                        continue
                    while height[k] < N and board[height[k]][k] == 0:
                        height[k] += 1
                    if height[k] == N:
                        top[k], height[k] = None, None
                        continue
                    
                    top[k] = board[height[k]][k]
                
                break
        
        if not erasing_step:
            break
    
    return answer

# board = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]
board = [[0, 2, 0, 0], [1, 2, 0, 4], [1, 2, 2, 4], [1, 1, 4, 4]]
# board = [
# [0,0,0,0,0,0,0,0,0,0],
# [0,0,0,2,2,0,0,0,0,0],
# [0,0,0,2,1,0,0,0,0,0],
# [0,0,0,2,1,0,0,0,0,0],
# [0,0,0,0,1,1,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0]
# ]
print(solution(board))