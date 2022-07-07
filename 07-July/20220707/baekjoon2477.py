K = int(input())
routes = [list(map(int, input().split())) for _ in range(6)]

ccwList = [None, 4, 3, 1, 2]

answer1 = 0
answer2 = 0
for i in range(-1, 5):
    if routes[i+1][0] == ccwList[routes[i][0]]:
        answer1 = max(answer1, routes[i][1] * routes[i+1][1])
    else:
        answer2 = routes[i][1] * routes[i+1][1]

print(K * (answer1 - answer2))