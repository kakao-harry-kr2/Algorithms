# 1:32:25

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
food = [[5] * N for _ in range(N)]
tree = [[[0] * 11 for _ in range(N)] for _ in range(N)]
move = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

next = [[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        for k in range(8):
            next_i, next_j = i + move[k][0], j + move[k][1]
            if 0 <= next_i < N and 0 <= next_j < N:
                next[i][j].append((next_i, next_j))

for _ in range(M):
    x, y, z = map(int, input().split())
    tree[x-1][y-1][z] += 1

for _ in range(K):
    for i in range(N):
        for j in range(N):
            """ 봄 """
            max_age = len(tree[i][j])
            limited_age = max_age - 1
            for age in range(1, max_age):
                if food[i][j] >= tree[i][j][age] * age:
                    food[i][j] -= tree[i][j][age] * age
                else:
                    # 나이가 age인 모든 나무들이 양분을 공급받지 못하는 경우
                    cnt = food[i][j] // age
                    food[i][j] -= cnt * age

                    """ 여름 : 죽은 나무들이 양분을 공급해줌 """
                    food[i][j] += age // 2 * (tree[i][j][age] - cnt)
                    tree[i][j][age] = cnt
                    limited_age = age
                    a = age + 1
                    while a < max_age:
                        food[i][j] += a // 2 * tree[i][j][a]
                        a += 1
                    break

            # 나이 1씩 증가 & 죽은 나무들 처리
            while limited_age > 0 and tree[i][j][limited_age] == 0:
                limited_age -= 1
            tree[i][j] = [0] + [tree[i][j][k] for k in range(limited_age+1)]
    
    """ 가을 """
    for i in range(N):
        for j in range(N):
            for age in range(5, len(tree[i][j]), 5):
                if tree[i][j][age] > 0:
                    for next_i, next_j in next[i][j]:
                        tree[next_i][next_j][1] += tree[i][j][age]
    
    """ 겨울 """
    for i in range(N):
        for j in range(N):
            food[i][j] += A[i][j]

answer = 0
for i in range(N):
    for j in range(N):
        answer += sum(tree[i][j])

print(answer)