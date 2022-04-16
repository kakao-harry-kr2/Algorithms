def solution(board, moves):
    answer = 0
    N = len(board)

    height = []
    for j in range(N):
        for i in range(N):
            if board[i][j] != 0:
                height.append(i)
                break
    
    stack = []
    for move in moves:
        move -= 1
        # 해당 번호에 인형이 없는 경우
        if height[move] == N:
            continue

        picked = board[height[move]][move]
        height[move] += 1

        if len(stack) > 0 and stack[-1] == picked:
            stack.pop()
            answer += 2
        else:
            stack.append(picked)

    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))