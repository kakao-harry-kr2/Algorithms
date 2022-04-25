from collections import deque

N, M, amount = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
x, y = map(lambda x: int(x) - 1, input().split())
passengers = [[None] * N for _ in range(N)]
for _ in range(M):
    sx, sy, ex, ey = map(int, input().split())
    passengers[sx-1][sy-1] = (ex-1, ey-1)

for _ in range(M):
    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True
    q = deque([(0, x, y)])
    next_passengers = []
    searching = False
    while q:
        dist, now_x, now_y = q.popleft()
        if passengers[now_x][now_y] != None:
            if not next_passengers or dist == next_passengers[0][0]:
                if amount >= dist:
                    next_passengers.append((dist, now_x, now_y))
                else:
                    print(-1) # 출발지로 이동할 수 없는 경우
                    exit()
            
            if next_passengers and dist > next_passengers[0][0]:
                next_passengers.sort(key=lambda x: (x[1], x[2]))
                dist, now_x, now_y = next_passengers[0]
                amount -= dist
                x, y = now_x, now_y
                searching = True
                # print("({0:d},{1:d})에 있는 손님에게 갈 때 {2:d}만큼의 연료".format(x, y, dist))
                break
        else:
            for k in range(4):
                next_x, next_y = now_x + move[k][0], now_y + move[k][1]
                if 0 <= next_x < N and 0 <= next_y < N and table[next_x][next_y] == 0 and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    q.append((dist+1, next_x, next_y))
    
    if not searching:
        if next_passengers:
            next_passengers.sort(key=lambda x: (x[1], x[2]))
            dist, now_x, now_y = next_passengers[0]
            amount -= dist
            x, y = now_x, now_y
        else:
            print(-1)
            exit()

    dest_x, dest_y = passengers[x][y]
    passengers[x][y] = None

    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True
    q = deque([(0, x, y)])
    searching = False
    while q:
        dist, now_x, now_y = q.popleft()
        if (now_x, now_y) == (dest_x, dest_y):
            if amount >= dist:
                amount += dist
                x, y = dest_x, dest_y
                searching = True
                # print("({0:d},{1:d})로 데려다 줄 때 {2:d}만큼의 연료".format(x, y, dist))
                break
            else:
                print(-1) # 목적지로 이동할 수 없는 경우
                exit()
        else:
            for k in range(4):
                next_x, next_y = now_x + move[k][0], now_y + move[k][1]
                if 0 <= next_x < N and 0 <= next_y < N and table[next_x][next_y] == 0 and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    q.append((dist+1, next_x, next_y))
    
    if not searching:
        print(-1)
        exit()

print(amount)