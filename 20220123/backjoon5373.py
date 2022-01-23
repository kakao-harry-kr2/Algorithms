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

def rotate(a, type):
    if type == '+':
        return rotate_clockwise(a)
    else:
        return rotate_counterclockwise(a)

direction2int = {'U': 0, 'D': 1, 'F': 2, 'B': 3, 'L': 4, 'R': 5}
directionChange = {'U': 'UFLBRD', 'D': 'DFRBLU', 'F': 'FURDLB', 'B': 'BULDRF', 'L': 'LUFDBR', 'R': 'RUBDFL'}

for _ in range(T):
    # 큐브 초기화
    up =    [['w'] * 3 for _ in range(3)]
    down =  [['y'] * 3 for _ in range(3)]
    front = [['r'] * 3 for _ in range(3)]
    back =  [['o'] * 3 for _ in range(3)]
    left =  [['g'] * 3 for _ in range(3)]
    right = [['b'] * 3 for _ in range(3)]

    main_total = [up] + [down] + [front] + [back] + [left] + [right]

    n = int(input())
    moveList = list(input().split())

    for move in moveList:
        space, type = move[0], move[1]
        total = [main_total[direction2int[directionChange[space][i]]] for i in range(6)]

        # 윗면 rotate
        total[0] = rotate(total[0], type)

        # 옆면 rotate
        rotate_type = 1 if type == '+' else -1

        # Todo