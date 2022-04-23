move = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def process(x, y, table, moveList, amount):
    next_x = x
    next_y = y
    for m in moveList:
        next_x, next_y = next_x + move[m][0], next_y + move[m][1]
    table[next_x][next_y] += amount
    table[x][y] -= amount

N = int(input())
table = [list(map(int, input().split())) + [0, 0] for _ in range(N)]
table += [[0] * (N+2)] + [[0] * (N+2)]

x, y = (N-1)//2, (N-1)//2
count = 0
stopping = False
while True:
    front, left, back, right = count % 4, (count+1) % 4, (count+2) % 4, (count+3) % 4
    for _ in range(count//2+1):
        x, y = x + move[front][0], y + move[front][1]
        amount = table[x][y]
        process(x, y, table, [front, front], int(amount * 0.05))
        process(x, y, table, [front, left], int(amount * 0.1))
        process(x, y, table, [front, right], int(amount * 0.1))
        process(x, y, table, [left, left], int(amount * 0.02))
        process(x, y, table, [left], int(amount * 0.07))
        process(x, y, table, [right], int(amount * 0.07))
        process(x, y, table, [right, right], int(amount * 0.02))
        process(x, y, table, [back, left], int(amount * 0.01))
        process(x, y, table, [back, right], int(amount * 0.01))
        process(x, y, table, [front], table[x][y])

        if x + y == 0:
            stopping = True
            break

    if stopping:
        break

    count += 1

answer = 0
for i in range(N):
    answer += table[i][-1]
    answer += table[i][-2]

answer += sum(table[-2]) + sum(table[-1])

print(answer)