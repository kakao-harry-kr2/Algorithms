def rotate_matrix(mat):
    row_len, column_len = len(mat), len(mat[0])
    ret_mat = [[0] * row_len for _ in range(column_len)]

    for r in range(row_len):
        for c in range(column_len):
            ret_mat[c][row_len-1-r] = mat[r][c]
    
    return ret_mat

def organize(fishbowls):
    N = len(fishbowls)

    # step 1
    min_num = min(fishbowls)
    for i in range(len(fishbowls)):
        if fishbowls[i] == min_num:
            fishbowls[i] += 1
    
    # step 2
    width, height = 1, 1
    idx = 1
    mat = [[fishbowls[0]]]
    while idx + height <= N:
        mat = rotate_matrix(mat)
        mat.append(fishbowls[idx:idx+height])
        idx += height
        width, height = height, width + 1
    
    # step 3
    diff = [[0] * width for _ in range(height)]
    for i in range(height):
        for j in range(width):
            # horizontal
            if j + 1 < width:
                value = abs(mat[i][j] - mat[i][j+1]) // 5
                diff[i][j] -= value if mat[i][j] >= mat[i][j+1] else -value
                diff[i][j+1] -= value if mat[i][j] < mat[i][j+1] else -value
            # vertical
            if i + 1 < height:
                value = abs(mat[i][j] - mat[i+1][j]) // 5
                diff[i][j] -= value if mat[i][j] >= mat[i+1][j] else -value
                diff[i+1][j] -= value if mat[i][j] < mat[i+1][j] else -value
    
    if idx != N:
        diff2 = [0] * len(fishbowls)

        # mat와 fishbowls[idx:]의 connected part
        value = mat[-1][-1] - fishbowls[idx]
        diff[-1][-1] -= value//5 if value >= 0 else -((-value)//5)
        diff2[idx] += value//5 if value >= 0 else -((-value)//5)

        # 나머지 fishbowls part
        for i in range(idx, N-1):
            value = fishbowls[i] - fishbowls[i+1]
            diff2[i] -= value//5 if value >= 0 else -((-value)//5)
            diff2[i+1] += value//5 if value >= 0 else -((-value)//5)

        fishbowls = [fishbowls[i] + diff2[i] for i in range(N)]
    
    for i in range(height):
        for j in range(width):
            mat[i][j] += diff[i][j]

    mat = rotate_matrix(mat)
    width, height = height, width
    for i in range(height):
        for j in range(width):
            fishbowls[i*width+j] = mat[i][j]
    
    # step 4
    mat = [fishbowls[N//2:N//4*3][::-1], fishbowls[N//4:N//2], fishbowls[:N//4][::-1], fishbowls[N//4*3:]]
    width, height = N//4, 4
    diff = [[0] * width for _ in range(height)]
    for i in range(height):
        for j in range(width):
            # horizontal
            if j + 1 < width:
                value = abs(mat[i][j] - mat[i][j+1]) // 5
                diff[i][j] -= value if mat[i][j] >= mat[i][j+1] else -value
                diff[i][j+1] -= value if mat[i][j] < mat[i][j+1] else -value
            # vertical
            if i + 1 < height:
                value = abs(mat[i][j] - mat[i+1][j]) // 5
                diff[i][j] -= value if mat[i][j] >= mat[i+1][j] else -value
                diff[i+1][j] -= value if mat[i][j] < mat[i+1][j] else -value

    for i in range(height):
        for j in range(width):
            mat[i][j] += diff[i][j]
    
    idx = 0
    for j in range(width):
        for i in reversed(range(height)):
            fishbowls[idx] = mat[i][j]
            idx += 1
    
    return fishbowls

N, K = map(int, input().split())
fishbowls = list(map(int, input().split()))

count = 0
while True:
    if max(fishbowls) - min(fishbowls) <= K:
        break

    fishbowls = organize(fishbowls)
    count += 1

print(count)