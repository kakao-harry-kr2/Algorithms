import time

def rotate_matrix(answer):
    row_length = len(answer)
    column_length = len(answer[0])

    result = [[0] * row_length for _ in range(column_length)]
    for r in range(row_length):
        for c in range(column_length):
            result[c][row_length-1-r] = answer[r][c]
    
    return result

def solution_impl(n, answer):
    count = (n + 1) // 2
    cycle = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    i, j = 0, -1
    number = 1
    for cnt in range(count):
        R = n - 1 - 2 * cnt 
        if R == 0: R = 1
        for _ in range(R):
            i += cycle[cnt%4][0]
            j += cycle[cnt%4][1]
            answer[i][j] = number
            number += 1
    
    return answer

def solution(n, clockwise):
    answer = [[0] * n for _ in range(n)]

    for _ in range(4):
        solution_impl(n, answer)
        answer = rotate_matrix(answer)

    if not clockwise:
        for i in range(n):
            answer[i] = answer[i][::-1]

    return answer

n = 1000
clockwise = False

start = time.time()

answer = solution(n, clockwise)

end = time.time()

print(end-start)