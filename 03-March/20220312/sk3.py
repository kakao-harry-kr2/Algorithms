import random, time

def solution(width, height, diagonals):
    dp = [[[0, 0] for _ in range(width+2)] for _ in range(height+2)]
    dp[0][0] = [1, 0]

    diagonal = [[False] * (width+2) for _ in range(height+2)]
    for x, y in diagonals:
        diagonal[y][x] = True

    for cnt in range(1, width+height+1):
        i = cnt if cnt <= height else height
        j = 0 if cnt <= height else cnt - height

        count = min(cnt+1, width+height+1-cnt)

        for k in range(count):
            dp[i-k][j+k][0] = (dp[i-k][j+k-1][0] + dp[i-k-1][j+k][0]) % 10000019
        
        for k in range(count):
            dp[i-k][j+k][1] = dp[i-k][j+k-1][1] + dp[i-k-1][j+k][1]

            if diagonal[i-k+1][j+k]:
                dp[i-k][j+k][1] += dp[i-k+1][j+k-1][0]
            if diagonal[i-k][j+k+1]:
                dp[i-k][j+k][1] += dp[i-k-1][j+k+1][0]
        
        dp[i-k][j+k][1] %= 10000019

    return dp[height][width][1]

width = 250
height = 250
diagonals = []
for cnt in range(width * height // 2):
    diagonals.append([random.randint(1, height), random.randint(1, width)])

start = time.time()

answer = solution(width, height, diagonals)
print(answer)

end = time.time()

print(end - start)