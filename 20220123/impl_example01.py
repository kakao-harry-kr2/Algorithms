import sys
input = sys.stdin.readline

def move2int(move):
    if move == 'L':
        return [0, -1]
    elif move == 'R':
        return [0, 1]
    elif move == 'U':
        return [-1, 0]
    elif move == 'D':
        return [1, 0]
    else:
        return [0, 0]

N = int(input())
moveList = list(map(move2int, input().split()))

i, j = 1, 1

for move in moveList:
    new_i = i + move[0]
    new_j = j + move[1]

    i = new_i if 1 <= new_i <= N else i
    j = new_j if 1 <= new_j <= N else j

print(i, j)