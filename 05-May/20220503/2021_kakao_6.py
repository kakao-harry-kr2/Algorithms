from collections import deque

move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
INF = 10 ** 9
answer = INF

def bfs(board, ir, ic, dr, dc):
    """ (ir, ic)에서 (dr, dc)까지 이동하는데 드는 최소 비용 """
    dist = [[7] * 4 for _ in range(4)]
    dist[ir][ic] = 0
    
    q = deque([(0, ir, ic)])
    while q:
        d, r, c = q.popleft()
        if (r, c) == (dr, dc):
            return d
        
        for k in range(4):
            # 방향키 이동
            next_r, next_c = r + move[k][0], c + move[k][1]
            if 0 <= next_r < 4 and 0 <= next_c < 4 and dist[next_r][next_c] == 7:
                dist[next_r][next_c] = d + 1
                q.append((d+1, next_r, next_c))

            # Ctrl + 방향키 이동
            shift_r, shift_c = r, c
            while 0 <= shift_r + move[k][0] < 4 and 0 <= shift_c + move[k][1] < 4:
                shift_r, shift_c = shift_r + move[k][0], shift_c + move[k][1]
                if board[shift_r][shift_c] > 0:
                    break
            
            if dist[shift_r][shift_c] == 7:
                dist[shift_r][shift_c] = d + 1
                q.append((d+1, shift_r, shift_c))

def dfs(board, num2pos:list, r, c, state:list, current):
    if state.count(True) == 7:
        global answer
        if current < answer:
            answer = current

        return

    for num in range(1, 7):
        if not state[num]:
            (num1r, num1c), (num2r, num2c) = num2pos[num]
            method1 = bfs(board, r, c, num1r, num1c) + bfs(board, num1r, num1c, num2r, num2c) + 2
            method2 = bfs(board, r, c, num2r, num2c) + bfs(board, num2r, num2c, num1r, num1c) + 2

            state[num] = True
            for i, j in num2pos[num]:
                board[i][j] = 0

            dfs(board, num2pos, num2r, num2c, state, current + method1)
            dfs(board, num2pos, num1r, num1c, state, current + method2)
            
            state[num] = False
            for i, j in num2pos[num]:
                board[i][j] = num

def solution(board, r, c):
    state = [True] * 7
    num2pos = [[] for _ in range(7)]
    for i in range(4):
        for j in range(4):
            if board[i][j] > 0:
                state[board[i][j]] = False
                num2pos[board[i][j]].append((i, j))

    dfs(board, num2pos, r, c, state, 0)

    return answer

# board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
board = [[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]]
print(solution(board, 0, 1))