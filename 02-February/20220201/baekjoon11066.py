import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    K = int(input())
    sizeList = list(map(int, input().split()))

    # dp table
    table = [[-1] * K for _ in range(K)]

    # 크기가 1인 sizeList에 대해 합치는 비용 X
    for i in range(K):
        table[i][i] = 0

    for i in range(1, K):
        for j in range(K-i):
            # j ~ j+i 에 대하여
            answer = int(1e9)
            for k in range(j, j+i):
                tmp = table[j][k] + table[k+1][j+i]
                if tmp < answer:
                    answer = tmp
            
            table[j][j+i] = answer + sum(sizeList[j:j+i+1])

    min_cost = table[0][K-1]
    print(min_cost)