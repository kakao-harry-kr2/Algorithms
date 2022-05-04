from collections import deque
INF = 10 ** 4

def solution(board):
    N = len(board)
    H = [[INF] * (N-1) for _ in range(N)]
    V = [[INF] * N for _ in range(N-1)]
    H[0][0] = 0 # 초기 상태
    
    q = deque([(0, 0, 0, 0)]) # dist, direction, i, j
    while q:
        dist, dir, i, j = q.popleft()
        # H 상태로 도착
        if dir == 0 and i == N-1 and j == N-2:
            return dist
        if dir == 1 and i == N-2 and j == N-1:
            return dist

        # H 상태에서
        if dir == 0:
            # H 상태로 이동
            if i >= 1 and not board[i-1][j] and not board[i-1][j+1] and H[i-1][j] == INF:
                H[i-1][j] = dist + 1
                q.append((dist+1, 0, i-1, j))
            if i + 1 < N and not board[i+1][j] and not board[i+1][j+1] and H[i+1][j] == INF:
                H[i+1][j] = dist + 1
                q.append((dist+1, 0, i+1, j))
            if j >= 1 and not board[i][j-1] and H[i][j-1] == INF:
                H[i][j-1] = dist + 1
                q.append((dist+1, 0, i, j-1))
            if j + 2 < N and not board[i][j+2] and H[i][j+1] == INF:
                H[i][j+1] = dist + 1
                q.append((dist+1, 0, i, j+1))
            
            # V 상태로 이동
            if i >= 1 and not board[i-1][j] and not board[i-1][j+1]:
                if V[i-1][j] == INF:
                    V[i-1][j] = dist + 1
                    q.append((dist+1, 1, i-1, j))
                if V[i-1][j+1] == INF:
                    V[i-1][j+1] = dist + 1
                    q.append((dist+1, 1, i-1, j+1))
            if i + 1 < N and not board[i+1][j] and not board[i+1][j+1]:
                if V[i][j] == INF:
                    V[i][j] = dist + 1
                    q.append((dist+1, 1, i, j))
                if V[i][j+1] == INF:
                    V[i][j+1] = dist + 1
                    q.append((dist+1, 1, i, j+1))
        
        # V 상태에서
        else:
            # H 상태로 이동
            if j >= 1 and not board[i][j-1] and not board[i+1][j-1]:
                if H[i][j-1] == INF:
                    H[i][j-1] = dist + 1
                    q.append((dist+1, 0, i, j-1))
                if H[i+1][j-1] == INF:
                    H[i+1][j-1] = dist + 1
                    q.append((dist+1, 0, i+1, j-1))
            if j + 1 < N and not board[i][j+1] and not board[i+1][j+1]:
                if H[i][j] == INF:
                    H[i][j] = dist + 1
                    q.append((dist+1, 0, i, j))
                if H[i+1][j] == INF:
                    H[i+1][j] = dist + 1
                    q.append((dist+1, 0, i+1, j))

            # V 상태로 이동
            if j >= 1 and not board[i][j-1] and not board[i+1][j-1] and V[i][j-1] == INF:
                V[i][j-1] = dist + 1
                q.append((dist+1, 1, i, j-1))
            if j + 1 < N and not board[i][j+1] and not board[i+1][j+1] and V[i][j+1] == INF:
                V[i][j+1] = dist + 1
                q.append((dist+1, 1, i, j+1))
            if i >= 1 and not board[i-1][j] and V[i-1][j] == INF:
                V[i-1][j] = dist + 1
                q.append((dist+1, 1, i-1, j))
            if i + 2 < N and not board[i+2][j] and V[i+1][j] == INF:
                V[i+1][j] = dist + 1
                q.append((dist+1, 1, i+1, j))

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))