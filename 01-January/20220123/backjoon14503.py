import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A, B, d = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

move = [[-1, 0], [0, 1], [1, 0], [0, -1]]
visited = [[A, B]]
check = 0

while True:
    # 1단계
    d = d - 1 if d > 0 else 3

    # 2단계
    next_A, next_B = A + move[d][0], B + move[d][1]
    check += 1
    if table[next_A][next_B] == 0 and [next_A, next_B] not in visited:
        A, B = next_A, next_B
        visited.append([A, B])
        check = 0
    
    # 3단계
    if check == 4:
        next_A, next_B = A + move[(d+2)%4][0], B + move[(d+2)%4][1]
        if table[next_A][next_B] == 1:
            break
        A, B = next_A, next_B
        check = 0

print(len(visited))