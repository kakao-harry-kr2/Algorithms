T = int(input())

move = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 북동남서
block = [None, [2, 3, 1, 0], [1, 3, 0, 2], [3, 2, 0, 1], [2, 0, 3, 1], [2, 3, 0, 1]]

for t in range(1, T + 1):
    N = int(input())
    table = [list(map(int, input().split())) + [5] for _ in range(N)] + [[5] * (N+1)]

    wormholeArr = [[] for _ in range(5)]
    for i in range(N):
        for j in range(N):
            if table[i][j] > 5:
                wormholeArr[table[i][j] - 6].append((i, j))

    wormhole = dict()
    for i in range(5):
        if wormholeArr[i]:
            p1, p2 = wormholeArr[i]
            wormhole[p1] = p2
            wormhole[p2] = p1

    max_score = 0
    visited = [[[False] * 4 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(N):
        for j in range(N):
            # 빈 공간에만 핀볼을 놓을 수 있음
            if table[i][j] != 0:
                continue
            
            for k in range(4):
                # 이미 다른 출발점을 통해 지나간 경우 : 최댓값에 기여 못함
                # if visited[i][j][k]:
                #     continue

                # (i, j)에서 방향 k로 출발
                now_i, now_j, dir = i, j, k
                score = 0
                while True:
                    start = True
                    # 방문 처리
                    # visited[now_i][now_j][dir] = True
                    next_i, next_j = now_i + move[dir][0], now_j + move[dir][1]

                    if (next_i, next_j) == (i, j) or table[next_i][next_j] == -1:
                        break

                    # 블록인 경우
                    if 1 <= table[next_i][next_j] <= 5:
                        score += 1
                        dir = block[table[next_i][next_j]][dir]

                    # 웜홀인 경우
                    elif table[next_i][next_j] > 5:
                        next_i, next_j = wormhole[(next_i, next_j)]

                    now_i, now_j = next_i, next_j

                if score > max_score:
                    max_score = score

    print("#{0:d} {1:d}".format(t, max_score))