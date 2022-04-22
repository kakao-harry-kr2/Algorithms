N = int(input())
seats = [[0] * N for _ in range(N)]
move = [(0, -1), (-1, 0), (0, 1), (1, 0)]
favorites = [None] * (N ** 2 + 1)

for _ in range(N**2):
    idx, *favorite = map(int, input().split())
    favorites[idx] = favorite
    score = [[None] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            empty_count = 0
            favorite_count = 0
            for k in range(4):
                next_i, next_j = i + move[k][0], j + move[k][1]
                if 0 <= next_i < N and 0 <= next_j < N:
                    if seats[next_i][next_j] == 0:
                        empty_count += 1
                    elif seats[next_i][next_j] in favorite:
                        favorite_count += 1
            
            score[i][j] = (favorite_count, empty_count)
    
    max_scored_seat, max_favorite, max_empty = None, -1, -1
    for i in range(N):
        for j in range(N):
            if seats[i][j] == 0 and (score[i][j][0] > max_favorite or (score[i][j][0] == max_favorite and score[i][j][1] > max_empty)):
                max_scored_seat = (i, j)
                max_favorite = score[i][j][0]
                max_empty = score[i][j][1]
    
    seats[max_scored_seat[0]][max_scored_seat[1]] = idx

answer = 0
neighbors = [0, 1, 10, 100, 1000]
for i in range(N):
    for j in range(N):
        count = 0
        for k in range(4):
            next_i, next_j = i + move[k][0], j + move[k][1]
            if 0 <= next_i < N and 0 <= next_j < N:
                if seats[next_i][next_j] in favorites[seats[i][j]]:
                    count += 1
        answer += neighbors[count]

print(answer)