import sys
input = sys.stdin.readline

T = int(input())

def rotate_clockwise(a):
    res = [[0] * 3 for _ in range(3)]
    for r in range(3):
        for c in range(3):
            res[c][2 - r] = a[r][c]
    return res

def rotate_counterclockwise(a):
    res = [[0] * 3 for _ in range(3)]
    for r in range(3):
        for c in range(3):
            res[2-c][r] = a[r][c]
    return res

for _ in range(T):
    # 큐브 초기화
    up =    [['w'] * 3 for _ in range(3)]
    down =  [['y'] * 3 for _ in range(3)]
    front = [['r'] * 3 for _ in range(3)]
    back =  [['o'] * 3 for _ in range(3)]
    left =  [['g'] * 3 for _ in range(3)]
    right = [['b'] * 3 for _ in range(3)]

    n = int(input())
    moveList = list(input().rstrip().split())

    for move in moveList:
        space, type = move[0], move[1]

        if space == 'U' and type == '+':
            up = rotate_clockwise(up)
            front[0], right[0], back[0], left[0] = right[0], back[0], left[0], front[0]
        elif space == 'U' and type == '-':
            up = rotate_counterclockwise(up)
            front[0], right[0], back[0], left[0] = left[0], front[0], right[0], back[0]
        elif space == 'D' and type == '+':
            down = rotate_clockwise(down)
            front[2], right[2], back[2], left[2] = left[2], front[2], right[2], back[2]
        elif space == 'D' and type == '-':
            down = rotate_counterclockwise(down)
            front[2], right[2], back[2], left[2] = right[2], back[2], left[2], front[2]
        elif space == 'F' and type == '+':
            front = rotate_clockwise(front)
            up[2][0], up[2][1], up[2][2], left[2][2], left[1][2], left[0][2], down[0][2], down[0][1], down[0][0], right[0][0], right[1][0], right[2][0] = left[2][2], left[1][2], left[0][2], down[0][2], down[0][1], down[0][0], right[0][0], right[1][0], right[2][0], up[2][0], up[2][1], up[2][2]
        elif space == 'F' and type == '-':
            front = rotate_counterclockwise(front)
            up[2][0], up[2][1], up[2][2], left[2][2], left[1][2], left[0][2], down[0][2], down[0][1], down[0][0], right[0][0], right[1][0], right[2][0] = right[0][0], right[1][0], right[2][0], up[2][0], up[2][1], up[2][2], left[2][2], left[1][2], left[0][2], down[0][2], down[0][1], down[0][0]
        elif space == 'B' and type == '+':
            back = rotate_clockwise(back)
            up[0][2], up[0][1], up[0][0], left[0][0], left[1][0], left[2][0], down[2][0], down[2][1], down[2][2], right[2][2], right[1][2], right[0][2] = right[2][2], right[1][2], right[0][2], up[0][2], up[0][1], up[0][0], left[0][0], left[1][0], left[2][0], down[2][0], down[2][1], down[2][2]
        elif space == 'B' and type == '-':
            back = rotate_counterclockwise(back)
            up[0][2], up[0][1], up[0][0], left[0][0], left[1][0], left[2][0], down[2][0], down[2][1], down[2][2], right[2][2], right[1][2], right[0][2] = left[0][0], left[1][0], left[2][0], down[2][0], down[2][1], down[2][2], right[2][2], right[1][2], right[0][2], up[0][2], up[0][1], up[0][0]
        elif space == 'L' and type == '+':
            left = rotate_clockwise(left)
            up[2][0], up[1][0], up[0][0], front[2][0], front[1][0], front[0][0], down[2][0], down[1][0], down[0][0], back[0][2], back[1][2], back[2][2] = back[0][2], back[1][2], back[2][2], up[2][0], up[1][0], up[0][0], front[2][0], front[1][0], front[0][0], down[2][0], down[1][0], down[0][0]
        elif space == 'L' and type == '-':
            left = rotate_counterclockwise(left)
            up[2][0], up[1][0], up[0][0], front[2][0], front[1][0], front[0][0], down[2][0], down[1][0], down[0][0], back[0][2], back[1][2], back[2][2] = front[2][0], front[1][0], front[0][0], down[2][0], down[1][0], down[0][0], back[0][2], back[1][2], back[2][2], up[2][0], up[1][0], up[0][0]
        elif space == 'R' and type == '+':
            right = rotate_clockwise(right)
            up[2][2], up[1][2], up[0][2], back[0][0], back[1][0], back[2][0], down[2][2], down[1][2], down[0][2], front[2][2], front[1][2], front[0][2] = front[2][2], front[1][2], front[0][2], up[2][2], up[1][2], up[0][2], back[0][0], back[1][0], back[2][0], down[2][2], down[1][2], down[0][2]
        elif space == 'R' and type == '-':
            right = rotate_counterclockwise(right)
            up[2][2], up[1][2], up[0][2], back[0][0], back[1][0], back[2][0], down[2][2], down[1][2], down[0][2], front[2][2], front[1][2], front[0][2] = back[0][0], back[1][0], back[2][0], down[2][2], down[1][2], down[0][2], front[2][2], front[1][2], front[0][2], up[2][2], up[1][2], up[0][2]
        else:
            pass

    for i in range(3):
        for j in range(3):
            print(up[i][j], end='')
        print()