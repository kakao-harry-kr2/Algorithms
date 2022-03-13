def rotate_matrix(answer):
    row_length = len(answer)
    column_length = len(answer[0])

    result = [[0] * row_length for _ in range(column_length)]
    for r in range(row_length):
        for c in range(column_length):
            result[c][row_length-1-r] = answer[r][c]
    
    return result