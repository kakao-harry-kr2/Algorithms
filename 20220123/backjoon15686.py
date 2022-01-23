from itertools import combinations

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

houseList = []
chickenList = []

for i in range(N):
    for j in range(N):
        if table[i][j] == 1:
            houseList.append([i, j])
        if table[i][j] == 2:
            chickenList.append([i, j])

answer = 4 * N * N

for comb in combinations(chickenList, M):
    chicken_distance = 0
    for house in houseList:
        chicken_distance += min(list(map(lambda x: distance(x, house), comb)))
    if chicken_distance < answer:
        answer = chicken_distance

print(answer)