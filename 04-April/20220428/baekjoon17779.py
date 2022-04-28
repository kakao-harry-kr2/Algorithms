# 00:32:37

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

answer = 10 ** 5

for x in range(0, N-2):
    for y in range(1, N-1):
        for d1 in range(1, min(N-1-x, y+1)):
            for d2 in range(1, min(N-x-d1, N-y)):
                count = [0, 0, 0, 0, 0]
                for i in range(N):
                    for j in range(N):
                        if i+j >= x+y and j-i <= y-x and j-i >= y-x-2*d1 and i+j <= x+y+2*d2:
                            count[4] += table[i][j]
                        
                        elif 0 <= i < x + d1 and 0 <= j <= y:
                            count[0] += table[i][j]
                        elif 0 <= i <= x + d2 and y < j < N:
                            count[1] += table[i][j]
                        elif x + d1 <= i < N and 0 <= j < y - d1 + d2:
                            count[2] += table[i][j]
                        else:
                            count[3] += table[i][j]
                
                value = max(count) - min(count)
                if value < answer:
                    answer = value

print(answer)