W, H, X, Y, P = map(int, input().split())

answer = 0
for _ in range(P):
    x, y = map(int, input().split())

    if X <= x <= X + W and Y <= y <= Y + H:
        answer += 1
    
    min_y = Y + H/2 - ((H/2) ** 2 - (x-X) ** 2) ** 0.5
    max_y = Y + H/2 + ((H/2) ** 2 - (x-X) ** 2) ** 0.5
    if X - H/2 <= x < X and min_y <= y <= max_y:
        answer += 1
    
    min_y = Y + H/2 - ((H/2) ** 2 - (x-X-W) ** 2) ** 0.5
    max_y = Y + H/2 + ((H/2) ** 2 - (x-X-W) ** 2) ** 0.5
    if X + W < x <= X + W + H/2 and min_y <= y <= max_y:
        answer += 1

print(answer)